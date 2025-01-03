from fastapi import FastAPI
from app.routers import users

app = FastAPI(
    title='Ecommerce API',
    version='1.0.0'
)

app.include_router(users.router)
