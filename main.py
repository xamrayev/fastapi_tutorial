from fastapi import FastAPI
from database import create_tables, delete_tables
from contextlib import asynccontextmanager

from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Baza ochishena")
    await create_tables()
    print("Baza gotova k rabote")
    yield
    print("Viklyucheniya")



app = FastAPI(lifespan=lifespan)
app.include_router(task_router)




