from fastapi import FastAPI
from auth.router import router as auth_router
from users.router import router as users_router
from models import create_tables

app = FastAPI()

create_tables()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Authentication API ya Rorisang ea sebetsa"}