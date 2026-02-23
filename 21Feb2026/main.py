from fastapi import FastAPI

MOCK_USERS = {
    1: {"name": "Alice", "role": "admin"},
    2: {"name": "Bob", "role": "user"},
    3: {"name": "Charlie", "role": "user"},
}

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return MOCK_USERS.get(user_id)


@app.get("/users")
def get_users(role: str | None = None):
    if role is not None:
        return [user for id, user in MOCK_USERS.items() if user.get("role") == role]
    else:
        return MOCK_USERS


@app.get("/")
def welcome():
    return {"message": "Welcome to my API"}


@app.get("/health")
def health():
    return {"status": "Healthy", "version": "1.0.0"}
