from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.controller.routes import router

app = FastAPI(
    title='Сервис для проведения лабораторной работы по теме \
            "Нагрузочное тестирование"',
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/api/docs")


@app.get("/api/", include_in_schema=False)
def bare_api_route():
    return RedirectResponse("/api/docs")


@app.get("/docs/", include_in_schema=False)
def wrong_docs():
    return RedirectResponse("/api/docs")


app.include_router(router)
