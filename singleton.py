class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


import warnings
warnings.filterwarnings('ignore')

import numpy as np
np.random.seed(0)

import optuna
import gc
from optuna.pruners import SuccessiveHalvingPruner
from optuna.integration import CatBoostPruningCallback
import joblib
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, f1_score

