import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from azureml.core import Dataset
from config import get_workspace

def train_and_save_model():
    ws = get_workspace()
    dataset = Dataset.get_by_name(ws, name='diabetes_dataset')
    df = dataset.to_pandas_dataframe()

    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, 'outputs/model.pkl')