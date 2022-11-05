from typing import List

from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from app.config.settings import email_settings


async def send_email(background_tasks: BackgroundTasks, emails: List[str], data: str) -> None:
    """Send email message in background."""
    message = MessageSchema(
        recipients=emails,
        body=data
    )
    conf = ConnectionConfig(**email_settings.dict())
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
