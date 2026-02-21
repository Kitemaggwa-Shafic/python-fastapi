from fastapi import FastAPI
from app.routes.issues import router as issues_router
 
# Create a FastAPI app instance
app = FastAPI()

#we are incluidng the importted issue_router with in our app to be visible in our projet
app.include_router(issues_router)
    
