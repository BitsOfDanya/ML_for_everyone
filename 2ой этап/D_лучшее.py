import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV, KFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE

data = pd.read_csv("data_D.csv")
data.fillna(0, inplace=True)
train_data = data[data['target'] != '?']
X = train_data.drop(['id', 'target'], axis=1)
y = train_data['target']

le = LabelEncoder()
y_enc = le.fit_transform(y)
sc = StandardScaler()
X_sc = sc.fit_transform(X)

X_train, X_val, y_train, y_val = train_test_split(X_sc, y_enc, test_size=0.2, random_state=42)

smote = SMOTE()
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)

xgb_model = XGBClassifier()

param_dist = {
    'n_estimators': range(100, 500, 50),
    'learning_rate': [0.05, 0.08, 0.1],
    'max_depth': [4, 5, 6],
    'colsample_bytree': [0.3, 0.4, 0.5],
    'subsample': [0.3, 0.4, 0.5]
}
random_search = RandomizedSearchCV(xgb_model, param_dist, n_iter=100, scoring='accuracy', n_jobs=-1, cv=KFold(5), random_state=42, verbose=2)
random_search.fit(X_train_sm, y_train_sm)

best_xgb = random_search.best_estimator_
print(f"Best parameters: {random_search.best_params_}")

y_pred = best_xgb.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
print(f"Validation Accuracy: {accuracy}")

X_all = sc.transform(data.drop(['id', 'target'], axis=1))
all_predictions = best_xgb.predict(X_all)

res_df = data[['id']].copy()
res_df['target'] = le.inverse_transform(all_predictions)
res_df.to_csv("submission_xgb_optimized.csv", index=False)
