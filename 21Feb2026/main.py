from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    return {"message": "Welcome to my API"}


@app.get("/health")
def health():
    return {"status": "Healthy", "version": "1.0.0"}
