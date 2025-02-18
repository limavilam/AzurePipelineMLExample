from azureml.core import Dataset, Datastore
from config import get_workspace

def upload_and_register_data():
    ws = get_workspace()
    datastore = ws.get_default_datastore()
    datastore.upload_files(files=['data/diabetes.csv'], target_path='diabetes-data/', overwrite=True)
    dataset = Dataset.Tabular.from_delimited_files(path=[(datastore, 'diabetes-data/diabetes.csv')])
    dataset.register(workspace=ws, name='diabetes_dataset', description='Diabetes dataset')