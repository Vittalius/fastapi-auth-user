from typing import Optional

from pydantic import BaseModel

from fastapi_auth_user.auth import auth_service
from fastapi_auth_user.users.schema import Token


class AuthUserData(BaseModel):
	email: Optional[str] = None
	password: str = ...
	username: Optional[str] = None


if __name__ == "__main__":
	user_data: AuthUserData = AuthUserData(
		email="user@example.com",
		password="password123",
		username="username123"
	)
	token: Token = auth_service.get_access_token(user_data)
	user = auth_service.get_user_by_token(token)
