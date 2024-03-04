from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from app.core.config import ProjectSettings, ResourcePaths
from app.core.database import create_tables_and_db, engine
from app.api.auth.services import auth_router


app = FastAPI(title=ProjectSettings.title,
              description=ProjectSettings.description,
              license_info=ProjectSettings.license_info)

app.mount("/static", StaticFiles(directory=ResourcePaths.static), name="static")
templates = Jinja2Templates(directory=ResourcePaths.templates)
auth = ResourcePaths.auth

app.include_router(auth_router)


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})



@app.on_event("startup")
def on_startup():
    create_tables_and_db(engine=engine)
    