import pandas as pd

filename = 'submission3.csv'
predictions = pd.read_csv(filename)

has_negative_values = any(predictions['target'] < 0)

if has_negative_values:
    print("В файле есть отрицательные значения.")
else:
    print("В файле нет отрицательных значений.")
