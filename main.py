from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get1():
    return 'Hello, world!'
    
