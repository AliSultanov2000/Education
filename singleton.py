class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer


import warnings
warnings.filterwarnings('ignore')

import numpy as np
np.random.seed(0)

import optuna 
import joblib
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, KFold


# DataSet creation
ar, y = make_classification(n_samples=10000, n_features=3, n_informative=2, 
                           n_redundant=0, class_sep = 0.2, shuffle=False, 
                           flip_y=0, n_clusters_per_class=2)


# DataFrame, label
df = pd.DataFrame(ar, columns = ['feat1', 'feat2', 'feat3'])
df['y'] = y


# Dataset
df = df.sample(frac=1).reset_index(drop=True)
df


# Data separate
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns='y').copy(), 
                                                    df['y'],
                                                    test_size=0.2)

# Let's look at X_train
X_train.sample(3)


# In this case we can use Pipeline (inner and outer), ColumnTransformer, custom classes, custom def function in Pipeline, bu we selected simple example to show OptunaSearchCV


# KFold strategy
kf = KFold(n_splits=5, shuffle=True, random_state=50)


# Define the model
clf = CatBoostClassifier(verbose=False)


# Define param distribution
# IMPORTANT: IN param_distrs we can use only optuna.distribution! For instance, we can't use list, np.array and e.t.c.
param_distrs = {
                'min_data_in_leaf': optuna.distributions.IntDistribution(1, 10),
                'iterations': optuna.distributions.IntDistribution(800, 1200, 100),
                }


# OptunaSearchCV 
opt_search = optuna.integration.OptunaSearchCV(clf,
                                               param_distrs,
                                               cv=kf,
                                               scoring='f1',
                                               n_trials=10,  # Important parameters! In total we have 10 combination of hyperparameters and it's all
                                               timeout=100)  # Important parameters! In total trial time = 100 second


# Let's get started 
opt_search.fit(X_train, y_train)

# Let's look at some statistics
opt_search.trials_dataframe().drop(columns=['number',
                                                   'user_attrs_mean_fit_time',
                                                   'user_attrs_mean_score_time',
                                                   'user_attrs_split0_test_score',
                                                   'user_attrs_split1_test_score',
                                                   'user_attrs_split2_test_score',
                                                   'user_attrs_split3_test_score',
                                                   'user_attrs_split4_test_score',
                                                   'user_attrs_std_fit_time',
                                                   'user_attrs_std_score_time',
                                                   'value']).rename(columns={'user_attrs_mean_test_score': 'mean_test_score', 'user_attrs_std_test_score': 'std_test_score'})


# Load optuna search 
opt_search_loaded = joblib.load('experiments.pkl')


# Let's look at some statistics. Everything is work! 
opt_search_loaded.trials_dataframe().drop(columns=['number',
                                                   'user_attrs_mean_fit_time',
                                                   'user_attrs_mean_score_time',
                                                   'user_attrs_split0_test_score',
                                                   'user_attrs_split1_test_score',
                                                   'user_attrs_split2_test_score',
                                                   'user_attrs_split3_test_score',
                                                   'user_attrs_split4_test_score',
                                                   'user_attrs_std_fit_time',
                                                   'user_attrs_std_score_time',
                                                   'value']).rename(columns={'user_attrs_mean_test_score': 'mean_test_score', 'user_attrs_std_test_score': 'std_test_score'})
