from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    role: str


MOCK_USERS = {
    1: {"name": "Alice", "role": "admin"},
    2: {"name": "Bob", "role": "user"},
    3: {"name": "Charlie", "role": "user"},
}

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = MOCK_USERS.get(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user


@app.get("/users")
def get_users(role: str | None = None):
    if role is not None:
        return [user for id, user in MOCK_USERS.items() if user.get("role") == role]
    else:
        return MOCK_USERS


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    new_id = len(MOCK_USERS) + 1
    MOCK_USERS[new_id] = user.model_dump()
    return MOCK_USERS.get(new_id)


@app.get("/")
def welcome():
    return {"message": "Welcome to my API"}


@app.get("/health")
def health():
    return {"status": "Healthy", "version": "1.0.0"}
