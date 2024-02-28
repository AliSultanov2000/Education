class GradientBoostingRegressor: 
    
    def __init__(self, gamma=5, n_estimators=100, max_depth=6, learning_rate=0.01, random_state=10):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate
        self.random_state = random_state
        self.gamma = gamma
    
    
    def loss_gradient(self, y_true, y_pred): 
        return y_true - y_pred
    

    def gamma_regul(self, tree):
        return self.gamma * tree.tree_.n_leaves
    

    def fit(self, X, y): 
        self.trees = []
        self.y_base = np.mean(y, axis=0)
        self.y_pred = self.y_base

        for _ in range(self.n_estimators):  # Последовательно обучаем каждое дерево 
            gradient = self.loss_gradient(y, self.y_pred) 
            clf = DecisionTreeRegressor(random_state=self.random_state, max_depth=self.max_depth)
            clf.fit(X, gradient)
            self.trees.append(clf)
            self.y_pred += self.learning_rate * clf.predict(X) + self.gamma_regul(clf)

    
    def predict(self, X):
        y_composition = self.y_base + self.learning_rate * np.sum([tree.predict(X) for tree in self.trees], axis=0)  # Предикт композиции
        y_gamma = np.sum([self.gamma_regul(tree) for tree in self.trees], axis=0)                                    # Регуляризация модели
        return y_composition + y_gamma    
