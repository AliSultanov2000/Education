"""
Учебный файл с реализацией основных паттернов проектирование, так как: 
   - Синглтон;
   - Адаптер;
   - Фасад; 
   - Строитель;
   - Фабрика;
   - Декоратор;
"""



class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


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


# 1. Define the Objective Function
def objective(trial: optuna.Trial):
    # Define hyperparameters
    # Define model (Pipeline)
    # Train and evaluate the model (cross-validation)
    # Return the evaluation metric
    pass

# 2. Create a Study Object
study = optuna.create_study(direction='maximize')

# 3. Run the Optimization Process
study.optimize(objective, n_trials=100)
