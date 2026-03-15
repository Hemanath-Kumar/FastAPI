from fastapi import FastAPI
from router.main_page import router
app=FastAPI()

app.include_router(router)