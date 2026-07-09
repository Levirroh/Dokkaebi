from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Dokkaebi server is alive"
    }