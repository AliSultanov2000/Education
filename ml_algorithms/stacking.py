from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


X, y = load_iris(return_X_y=True)

estimators = [
     ('rf', RandomForestClassifier(n_estimators=10, random_state=42))
     ('svr', make_pipeline(StandardScaler(),
                           LinearSVC(dual="auto", random_state=42)))
             ]


skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

clf = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression(), cv=skfold)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

clf.fit(X_train, y_train)

# Check the results on train, test
print(f'Metric on train: {clf.score(X_train, y_train)}')
print(f'Metric on test: {clf.score(X_test, y_test)}')
