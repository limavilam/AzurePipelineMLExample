#from scripts.load_data import load_and_save_data
#from scripts.upload_data import upload_and_register_data
#from scripts.train_model import train_and_save_model
from load_data import load_and_save_data
from upload_data_azure import upload_and_register_data
from train_model import train_and_save_model

if __name__ == "__main__":
    # 1. Cargar y guardar datos
    load_and_save_data()

    # 2. Subir y registrar datos en Azure ML
    upload_and_register_data()

    # 3. Entrenar y guardar el modelo
    train_and_save_model()