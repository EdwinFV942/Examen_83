from fastapi import APIRouter
from schemas.auth_schema import Login
from controllers import auth_controller

router = APIRouter(tags=["Auth"])

@router.post("/login")
def login(user: Login):
    return auth_controller.login(user)