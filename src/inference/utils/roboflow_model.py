from roboflow import Roboflow

def init_model(config):
    rf = Roboflow(api_key=config["roboflow"]["api_key"])
    model = rf.workspace(config["roboflow"]["workspace"])\
               .project(config["roboflow"]["project"])\
               .version(config["roboflow"]["version"])\
               .model
    return model
