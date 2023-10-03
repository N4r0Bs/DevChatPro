from pathlib import Path
from enum import StrEnum, auto, Enum

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
    
class DatabaseConfiguration(object):
    
    SQLITE =  f"sqlite:///{Path(__file__).parent}/sqlite_database.db"


class CrudMethods(Enum):
    FIND_ONE = "FIND_ONE"
    FIND_MANY = "FIND_MANY"
    UPDATE_ONE = "UPDATE_ONE"
    UPDATE_MANY = "UPDATE_MANY"
    PATCH_ONE = "PATCH_ONE"
    PATCH_MANY = "PATCH_MANY"
    UPSERT_ONE = "UPSERT_ONE"
    UPSERT_MANY = "UPSERT_MANY"
    CREATE_ONE = "CREATE_ONE"
    CREATE_MANY = "CREATE_MANY"
    DELETE_ONE = "DELETE_ONE"
    DELETE_MANY = "DELETE_MANY"
    POST_REDIRECT_GET = "POST_REDIRECT_GET"
    FIND_ONE_WITH_FOREIGN_TREE = "FIND_ONE_WITH_FOREIGN_TREE"
    FIND_MANY_WITH_FOREIGN_TREE = "FIND_MANY_WITH_FOREIGN_TREE"

    @staticmethod
    def get_table_full_crud_method():
        return [CrudMethods.FIND_MANY, CrudMethods.CREATE_MANY, CrudMethods.UPDATE_MANY, CrudMethods.PATCH_MANY,
                CrudMethods.DELETE_MANY]

    @staticmethod
    def get_declarative_model_full_crud_method():
        return [CrudMethods.FIND_MANY, CrudMethods.FIND_ONE,
                CrudMethods.UPDATE_MANY, CrudMethods.UPDATE_ONE,
                CrudMethods.PATCH_MANY, CrudMethods.PATCH_ONE, CrudMethods.CREATE_MANY,
                 CrudMethods.DELETE_MANY, CrudMethods.DELETE_ONE, CrudMethods.FIND_ONE_WITH_FOREIGN_TREE,
                 CrudMethods.FIND_MANY_WITH_FOREIGN_TREE]


