import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

X = train.drop(columns=['target', 'id'])
y = train['target']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(64, activation='relu'),
    BatchNormalization(),
    Dropout(0.2),
    Dense(1, activation='linear')
])

model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

early_stopping = EarlyStopping(monitor='val_loss', patience=40, restore_best_weights=True)

model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=600, batch_size=25, callbacks=[early_stopping])

y_pred = np.maximum(0, model.predict(X_val).flatten())

def smape(y_true, y_pred):
    return 1 - np.mean(2 * np.abs(y_true - y_pred) / (np.abs(y_true) + np.abs(y_pred)))

nn_smape = smape(y_val, y_pred)

X_test_scaled = scaler.transform(test.drop(columns=['id']))
test_predictions = np.maximum(0, model.predict(X_test_scaled).flatten())

submission = pd.DataFrame({'id': test['id'], 'target': test_predictions})
submission.to_csv('submission_C.csv', index=False)

print(f"SMAPE резы: {nn_smape}")
