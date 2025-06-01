#!/usr/bin/env python

import sys
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
sys.path.append('src')
import fruitdb

fruitapi = FastAPI()
db = fruitdb.fruitdb()

@fruitapi.get("/")
async def read_root() -> str:
    return PlainTextResponse("Hello from fruitapi")

@fruitapi.get("/fruit/count")
async def get_fruit_count() -> int:
    return db.count()

@fruitapi.get("/fruit/all")
async def get_all_fruits() -> list[fruitdb.fruit]:
    return db.get_all()

@fruitapi.get("/fruit/{fruit_id}")
async def get_fruit_by_id(fruit_id: int) -> fruitdb.fruit:
    try:
        return db.get_by_id(fruit_id)
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err)) from err

@fruitapi.post("/fruit")
async def add_fruit(newfruit: fruitdb.fruit) -> str:
    try:
        db.put(newfruit)
        return "OK"
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err)) from err

@fruitapi.delete("/fruit/all")
async def delete_all_fruit() -> str:
    db.delete_all()
    return "OK"

@fruitapi.delete("/fruit/{fruit_id}")
async def delete_fruit_by_id(fruit_id: int) -> str:
    try:
        db.delete(fruit_id)
        return "OK"
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err)) from err

if __name__ == "__main__":
    print("This program must be invoked with fastapi, not directly.")
    sys.exit(1)
