from fastapi import FastAPI, HTTPException
from calculator import Calculator

app = FastAPI()
calc = Calculator()

@app.get("/add/")
async def add(a: int, b: int):
    return {"sum": calc.add(a, b)}

@app.get("/subtract/")
async def subtract(a: int, b: int):
    return {"difference": calc.subtract(a, b)}

@app.get("/multiply/")
async def multiply(a: int, b: int):
    return {"product": calc.multiply(a,b)}

@app.get("/divide/")
async def divide(a: int, b: int):
    try:
        return {"quotient": calc.divide(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))