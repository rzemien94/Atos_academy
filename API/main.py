# uvicorn main:app --reload -> potem wybrać link i dpoisać /docs żeby coś było widać :)
from fastapi import FastAPI

import GetStatistics

app = FastAPI()


@app.get("/stats")
async def stats(url: str):
    statistics = GetStatistics.get_statistics(url)
    return statistics
