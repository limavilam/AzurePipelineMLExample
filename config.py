from azureml.core import Workspace



def get_workspace():
    # Conectarse al área de trabajo
    ws = Workspace.from_config('/Users/linaavilamoreno/Library/CloudStorage/OneDrive-Personal/Documentos/AzurePipelineMLExample/config.json')

    print("Nombre del área de trabajo:", ws.name)
    return ws