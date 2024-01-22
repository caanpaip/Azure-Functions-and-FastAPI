import azure.functions as func

# from WrapperFunction import register as fastapi_app
from WrapperFunction import app as fastapi_app

app = func.AsgiFunctionApp(app=fastapi_app)