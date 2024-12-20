from fastapi import FastAPI

from app.api.main import api_router
from app.core.config import settings
from app.core.db import db_instance

db_instance.Base.metadata.create_all(bind=db_instance.engine)

app = FastAPI(
    title=settings.SERVICE_NAME, 
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "user-service-v1 running..."}
