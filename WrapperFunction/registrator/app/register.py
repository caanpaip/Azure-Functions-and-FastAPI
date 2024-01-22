from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from azure.cosmos import CosmosClient, PartitionKey
import uuid
import json
import os
import pytz
from datetime import datetime, date
from collections import deque
from dotenv import load_dotenv

load_dotenv()
COSMOS_CSTRING = os.getenv("COSMOS_CSTRING")

print(COSMOS_CSTRING)

register = APIRouter()

class Params(BaseModel):
    
    user:str = Field(description="User name")
    password:str = Field(description="Acess password")
    app_name:str = Field(description="Application name", examples=['streamlit_playground','chat_gpt'])
    status:str = Field(description="application name: ['ativo','inativo']")
    profile:str = Field(description="user profile: ['adm','guest']")
    max_inter:int = Field(description="User Maximum interactions allowed in the application")
    dt_exp:date = Field(description="Access expiration date. Format: yyyy-mm-dd")
    

app_name = "register_genai"
@register.post(f"/{app_name}/")
async def register_genai(req: Params):
    
    dict_params = req.model_dump()
    
    ## Cosmos conection
    client = CosmosClient.from_connection_string(COSMOS_CSTRING)
    ##  Creating Database 
    DATABASE_NAME = "genai"
    database = client.create_database_if_not_exists(id=DATABASE_NAME)
    ## Creating container
    CONTAINTER_REGISTER = "register-app-genai"
    key_path_register = PartitionKey(path = "/app_name")
    container_register = database.create_container_if_not_exists(id=CONTAINTER_REGISTER, partition_key = key_path_register  )
    
    ## creating new fields
    dict_params["dt_exp"] = dict_params["dt_exp"].strftime("%Y-%m-%d")
    dict_params["dt_incl"] = datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("%Y-%m-%d %H:%M:%S")
    dict_params["id"] = str( uuid.uuid4() ) 
    deque_dict = deque( dict_params.items() )       
    deque_dict.rotate(1)
    dict_params = dict(deque_dict)
    
    ## include in container
    container_register.create_item(dict_params)

    return dict_params