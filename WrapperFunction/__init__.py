from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from WrapperFunction.registrator.app.register import register


app = FastAPI()

@app.get("/")
async def root():
    return {"message":"GenAI Microservices"}


app.include_router(register, tags=["Register"])

##########################################################


def custom_openapi():
    
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title = "GenAI",
        version = "0.0.1",
        summary = "GenAI API's",
        description = "APIs created to implements generative AI solutions.",
        routes = app.routes
    )
    
    openapi_schema["info"]["x-logo"] = {
        "url":"https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    
    app.openapi_schema = openapi_schema
    
    return app.openapi_schema

app.openapi = custom_openapi
