from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Создаем объект безопасности
security = HTTPBasic()

# Простейшая "база данных" пользователей
valid_users = {
    "admin": "password123",
    "user": "12345"
}

# Модель данных
class NumbersRequest(BaseModel):
    a: float
    b: float

# Функция проверки учетных данных
def validate_user(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password

    if valid_users.get(username) != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Защищенный маршрут для сложения
@app.post("/sum")
def add_numbers(
    request: NumbersRequest,
    username: str = Depends(validate_user)
):
    result = request.a + request.b
    return {
        "result": result,
        "message": f"Successfully added by user '{username}'"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
