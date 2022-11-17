from fastapi import FastAPI, HTTPException, status
from dotenv import load_dotenv
from web3 import Web3
import os

load_dotenv()
alchemy_url = os.environ["ALCHEMY_URL"]
w3 = Web3(Web3.HTTPProvider(alchemy_url))

app = FastAPI()

is_connected = w3.isConnected()

@app.get("/")
def root():
    return {"Message" : "Welcome to my API"} 

@app.get("/connected")
def get_connect():
    return {"Connection" : is_connected}

@app.get("/latest")
def get_latest_block():
    latest_block = w3.eth.get_block("latest")
    if not is_connected:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                detail=f"Node connection unsuccessful")
    print(latest_block)
    return {"latest Block Number" : latest_block.number}
    

@app.get("/block/{num}")
def get_block_by_number(num: int):
    block = w3.eth.get_block(num)
    print(block)
    return {"block number" : block.number}
    
