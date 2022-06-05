# uvicorn main:app --reload
from fastapi import FastAPI

import GetStatistics

app = FastAPI()


@app.get("/stats")
async def stats(url: str):
    statistics = GetStatistics.get_statistics(url)
    return statistics
