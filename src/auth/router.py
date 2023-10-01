from fastapi import (
	APIRouter,
	Depends,
)
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from users.schema import UserAuth, Token

from .auth import auth_service
from database import (
	Database,
	db_helper
)

auth_router = APIRouter(
	prefix='/api',
	tags=["Authentication"],
	dependencies=[],
	responses={404: {"description": "Not found"}},
)


@auth_router.post("/login", response_model=Token, status_code=200)
def login_user(
		user_data: OAuth2PasswordRequestForm = Depends(),
		db: Database = Depends(db_helper.session_dependency)
):
	return auth_service.get_access_token(db, user_data)


@auth_router.get("/profile/me", response_model=UserAuth)
def get_user_by_token(
		token: str = Depends(auth_service.oauth2_scheme),
		db: Database = Depends(db_helper.session_dependency)
):
	return auth_service.get_user_by_token(db, token)


templates = Jinja2Templates(directory="templates")
