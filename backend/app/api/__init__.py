from fastapi import APIRouter

from .users.routes import router as user_router
from .auth.routes import router as auth_router

router = APIRouter()
router.include_router(user_router, tags=['User'], prefix='/user')
router.include_router(auth_router, tags=['Auth'], prefix='/auth')
