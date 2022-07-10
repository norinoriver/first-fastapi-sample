from dotenv import load_dotenv
import os
dotenv_path="./.dockerenv/dev.env" # TODO: setting run xargs
load_dotenv(dotenv_path=dotenv_path)

from fastapi import FastAPI
from api.routers import task, done, token, user


app = FastAPI()

app.include_router(token.router)
app.include_router(user.router)
app.include_router(task.router)
app.include_router(done.router)