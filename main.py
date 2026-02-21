from fastapi import FastAPI
#from app.routes import issues
 
# Create a FastAPI app instance
app = FastAPI()

@app.get("/api")
def check_api():
    return {"status", "ok"}
    
