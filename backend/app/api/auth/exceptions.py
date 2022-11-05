from fastapi import HTTPException, status


class BaseAPIException(HTTPException):
    headers = {"WWW-Authenticate": "Bearer"}


class AuthorizationException(BaseAPIException):
    def __init__(self, detail=None):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = detail or "Could not validate credentials"


class VerifyException(BaseAPIException):
    def __init__(self, detail=None):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = detail or "You need verify your email first"
