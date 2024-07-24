#=============================================================================#
#         Design Machine learning software model to Classification problem.   #
#.                   Universidad Nacional de Colombia.                        #
#.                              2024.                                         #
#=============================================================================#



# Import Libraries ------------
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import tarfile
from pathlib import Path
import urllib.request
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score


# download dataset ---------

def load_titanic_data():
    tarball_path = Path("datasets/titanic.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/titanic.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as titanic_tarball:
            titanic_tarball.extractall(path="datasets")
    return [pd.read_csv(Path("datasets/titanic") / filename)
            for filename in ("train.csv", "test.csv")]
    
train, test = load_titanic_data()
print('===='*32)
print(train.head())
print('===='*32)

# PassengerId: a unique identifier for each passenger
# Survived: that's the target, 0 means the passenger did not survive, while 1 means he/she survived.
# Pclass: passenger class.
# Name, Sex, Age: self-explanatory
# SibSp: how many siblings & spouses of the passenger aboard the Titanic.
# Parch: how many children & parents of the passenger aboard the Titanic.
# Ticket: ticket id
# Fare: price paid (in pounds)
# Cabin: passenger's cabin number
# Embarked: where the passenger embarked the Titanic


# Design dataset to train models -------

train_data = train.set_index("PassengerId")
test_data = test.set_index("PassengerId")


# Exploratory Data Analysis ----------

print(train\
    .isnull()\
        .mean())

train_missing = train\
    .isnull()\
        .mean()

train_missing = pd.DataFrame(train_missing.reset_index(name='Total')).rename(columns={'index':'Variable'})

import seaborn as sns 

sns.barplot(x='Variable',
            y='Total',
            data=train_missing)
plt.show()

## Pipeline -----------

num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])


cat_pipeline = Pipeline([
    ('ordinal_encoder', OrdinalEncoder()),
    ('imputer',SimpleImputer(strategy='most_frequent')),
    ('cat_encoder',OneHotEncoder())
])


num_attribs = ["Age", "SibSp", "Parch", "Fare"]
cat_attribs = ["Pclass", "Sex", "Embarked"]

preprocess_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", cat_pipeline, cat_attribs),
    ])




# Pipeline application ----------

X_train = preprocess_pipeline.fit_transform(train)
print('==='*32)
print('Transform train data with Pipeline')
print(X_train)
print('==='*32)

y_train = train["Survived"]


### Modelling -----------------


def evaluate_models(X_train, y_train):

    results = []

    # Random Forest
    forest_clf = RandomForestClassifier(n_estimators=100, random_state=42)
    forest_scores = cross_val_score(forest_clf, X_train, y_train, cv=10)
    results.append(('Random Forest', forest_scores.mean()))

    # Support Vector Machine
    svm_clf = SVC(gamma="auto")
    svm_scores = cross_val_score(svm_clf, X_train, y_train, cv=10)
    results.append(('SVM', svm_scores.mean()))

    # K-Nearest Neighbors
    knn_clf = KNeighborsClassifier()
    knn_scores = cross_val_score(knn_clf, X_train, y_train, cv=10)
    results.append(('KNN', knn_scores.mean()))


    results_df = pd.DataFrame(results, columns=['Model', 'Score'])
    results_df = results_df.sort_values(by='Score', ascending=False).reset_index(drop=True)


    best_model = results_df.iloc[0]


    print('==='*32)
    print('Model Performance')
    print(results_df)
    print('==='*32)
    print(f'The best model is: {best_model["Model"]} with a score of {best_model["Score"]:.4f}')
    print('==='*32)

    return results_df


results_df = evaluate_models(X_train, y_train)
print(results_df)


### Fine Tunning model ---------

from sklearn.metrics import classification_report
svm_clf = SVC()
param_grid = {'C': [0.1, 1, 10, 100, 1000],
              'gamma': [1, 0.1, 0.01,0.001,'auto'],
              'kernel': ['rbf','linear']}

grid = GridSearchCV(svm_clf, 
                    param_grid, 
                    cv=3, 
                    n_jobs=-1)
grid.fit(X_train, y_train)


print("Best parameters found:", grid.best_params_)

SVM_scores = cross_val_score(grid.best_estimator_, 
                            X_train, 
                            y_train, 
                            cv=3)

print("SVM Score with Grid Search: ",SVM_scores.mean())


# # Usar el mejor estimador para predecir sobre el conjunto de prueba
# y_pred = grid.best_estimator_.predict(X_test)

# # Generar e imprimir el informe de clasificación
# report = classification_report(y_test, y_pred)
# print("Classification Report:\n", report)
## predictions ------------


