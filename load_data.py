from sklearn.datasets import load_diabetes
import pandas as pd

def load_and_save_data():
    diabetes = load_diabetes()
    df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    df['target'] = diabetes.target
    df.to_csv('data/diabetes.csv', index=False)