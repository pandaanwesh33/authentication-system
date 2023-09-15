from fastapi import FastAPI
from services.registration import router as registration_router
from database import db

app = FastAPI()

# This code includes the registration router under the /auth prefix, so the registration route will be accessible at /auth/register.
app.include_router(registration_router, prefix="/auth")