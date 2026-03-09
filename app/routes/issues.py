#for no DB, we shall our own id
import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, UpdateIssue, IssueOut, IssueStatus

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


#post method, we are adding on status code
@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(issue:IssueCreate):
    """Creating an issue"""
    issues = load_data()
    #we are rapping our new issue in a dictionary 
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": issue.title,
        "description": issue.description,
        "priority": issue.priority,
        "status": IssueStatus.open,
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue


#Getting a single issue using its ID
@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str):
    """" Retrieve a Specific Issue by ID """
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue Not found")


#Update Issue
@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: str, payload: UpdateIssue):
    """" Updating an Issue """
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            updated_issue = issue.copy()
            if payload.title is not None:
                updated_issue["title"] = payload.title
            if payload.description is not None:
                updated_issue["description"] = payload.description
            if payload.priority is not None:
                updated_issue["priority"] = payload.priority
            if payload.status is not None:
                updated_issue["status"] = payload.status
            
            issue[index] = updated_issue
            save_data(issues)
            return updated_issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="issue not found in DB")




