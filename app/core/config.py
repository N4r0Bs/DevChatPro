from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from fastapi.templating import Jinja2Templates

class ProjectSettings(object):
    title = "DevChatPro"
    description = "DevChatPro is a web application designed to assist developers in managing their projects, tracking progress, and facilitating communication through real-time chat rooms."
    summary = None
    version = "0.0.1"
    contact = {"name": "Aleksa Lukic",
               "email": "aleksalukic92@web.de"}
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT"}
    
class ResourcePaths(object):
    static = Path(__file__).parent.parent / "static"
    templates = Path(__file__).parent.parent / "templates"
    auth = Path(__file__).parent.parent / "templates" / "auth"


class DatabaseConfiguration(object):
    SQLITE =  f"sqlite:///{Path(__file__).parent}/sqlite_database.db"

class JWTConfiguration(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8").items()
    
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
    

jwt_config = JWTConfiguration()