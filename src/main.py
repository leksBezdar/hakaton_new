from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.auth.routers import router as auth_router
from src.api.routers import router as api_router

app = FastAPI(
    title='AsQi'
)

app.include_router(auth_router, tags=["Registration"])
app.include_router(api_router, tags=["Api"])



@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <a href="http://127.0.0.1:8000/docs"><h1>Documentation</h1></a><br>
    <a href="http://127.0.0.1:8000/redoc"><h1>ReDoc</h1></a>
    """