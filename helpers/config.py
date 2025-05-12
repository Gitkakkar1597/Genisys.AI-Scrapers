from typing import Optional
from pydantic import BaseSettings, Field 

class Settings(BaseSettings):
    
    
    mongo_uri: str = Field(... , env="MONGO_URI")
    mongo_db: str = Field(... , env="MONGO_DB")
    
    
    
    
    
    
    class Config:
        
        
        env_file = "secrets/.env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        
        

# Global Settings instance

settings = Settings()
