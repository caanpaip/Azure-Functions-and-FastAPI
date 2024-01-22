import azure.functions as func

from WrapperFunction.main import app as fastapi_app

app = func.AsgiFunctionApp(app=fastapi_app)