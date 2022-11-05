import logging

from fastapi import APIRouter, status, HTTPException, Depends, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm

from app.api.auth.dependencies import get_current_user
from app.api.auth.exceptions import AuthorizationException, VerifyException
from app.api.auth.schemas import CreateUserSchema, Token, VerifyUserSchema
from app.api.auth.services import authenticate_user, verification_user
from app.api.auth.utils import hash_data, create_access_token, send_verification_code

from app.api.users.schemas import UserBaseSchema
from app.api.users.utils import get_user_by_email
from app.api.users.models import User

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserBaseSchema)
async def register_new_user(request: CreateUserSchema, background_tasks: BackgroundTasks):
    """
    Create new user
    """
    user_email = request.email.lower()
    user = await get_user_by_email(user_email)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Account already exist')
    try:
        request.password = hash_data(request.password)
        del request.password_confirm
        code = await send_verification_code(user_email, background_tasks)
        created_user = User(
            email=user_email,
            hashed_password=request.password,
            verification_code=hash_data(code)
        )
        await created_user.insert()
    except Exception as e:
        error_msg = "Error during creating user"
        logger.error(f'{error_msg}: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error_msg)
    else:
        return created_user.dict()


@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise AuthorizationException("Incorrect username or password")
    if not user.verified:
        raise VerifyException
    access_token = await create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/verify", status_code=status.HTTP_200_OK)
async def verify_user(request: VerifyUserSchema):
    user = await verification_user(request.email, request.verification_code)
    if not user:
        raise VerifyException(detail='Not verified')
    await user.set({User.verified: True})
    return "User has been successfully verified"


@router.get("/me")
async def get_user_from_token(current_user: User = Depends(get_current_user)):
    """
    Get user from token
    """
    return current_user
