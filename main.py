from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Authentication API ya Rorisang ea sebetsa"}