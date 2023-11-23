from fastapi import FastAPI, Request
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from core import ORIGINS
from controller import rag_router
import sys

__import__('pysqlite3')


sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rag_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="app:app", host="0.0.0.0", port=8000, workers=4)
