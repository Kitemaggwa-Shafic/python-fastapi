#for no DB, we shall our own id
import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, UpdateIssue, IssueOut

from app.storage import load_data, save_data

#initialising our APIRouter to a var called router, witha prefix of issues 
#to help us have api with may be version etc
router = APIRouter(prefix="/api/v1/issues", tags=["issues"])



#using the @router decorator and the diffrent methods
# so this .get g=will use a response model and return it as a list uing the issueout schema
@router.get("/issues", response_model=list[IssueOut])
#we can have our function to manage the data
def get_issues():
    """REtrieve all issues back """
    issues = load_data()
    return issues  