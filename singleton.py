class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance

# Data separation
X, y = make_regression(n_features=4, n_informative=2, random_state=50)
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, random_state=50)

# Scaling 
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Set alphas, model, coef path 
alphas = np.logspace(-7, 4, 10).tolist()  # Задаём параметр alpha

# Check regularization parameters 
def check_regularizarion(model, alphas): 
    df_result = pd.DataFrame(columns=["alpha", "train_metric", "test_metric"])
    for idx_alpha in range(len(alphas)):
        alpha = alphas[idx_alpha]
        model.set_params(alpha=alpha)
        model.fit(X_train, y_train)
        print(model.coef_)  # Show weights for the model
        
        train_score = model.score(X_train, y_train)  # Score on train
        test_score = model.score(X_test, y_test)  # Score on test
        df_result.loc[idx_alpha] = [alpha, train_score, test_score]
    print(df_result)


print('\nCoefficient for Lasso')
check_regularizarion(Lasso(), alphas)

print('\nCoefficient for Ridge')
check_regularizarion(Ridge(), alphas)
gc.collect()

# ElasticNet: example of creation model

l1_ratios = list(np.linspace(0, 1, 5))  # l1_ratio: [0, 1]
# For l1_ratio = 0 the penalty is an L2 penalty. For l1_ratio = 1 it is an L1 penalty
print(f'l1_ratios = {l1_ratios}')
elasticnet = ElasticNet(alpha=50, l1_ratio=0.5)  # Example
