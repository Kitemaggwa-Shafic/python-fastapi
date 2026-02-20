from fastapi import FastAPI
 
# Create a FastAPI app instance
app = FastAPI()

@app.get("/api")
def check_api():
    return {"status", "ok"}
