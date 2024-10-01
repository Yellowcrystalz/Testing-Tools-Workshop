from fastapi import FastAPI, HTTPException
from bank import Bank

app = FastAPI()
bank = Bank()

@app.post("/accounts/")
def create_account(id: str):
    try:
        bank.create_account(id)
        return {"message", f"Account {id} has been created"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/deposit/")
def deposit(id: str, amount: int):
    try:
        bank.get_account(id).deposit(amount)
        return {"message", f"Deposited {amount} into Account {id}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/withdrawl/")
def withdrawl(id: str, amount: int):
    try:
        bank.get_account(id).withdrawl(amount)
        return {"message", f"Withdrew {amount} into Account {id}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/balance/")
def check_balance(id: str):
    try:
        return {"balance": bank.get_account(id).get_balance()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


    