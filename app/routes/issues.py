from fastapi import APIRouter

#initialising our APIRouter to a var called router, witha prefix of issues 
#to help us have api with may be version etc
router = APIRouter(prefix="/api/v1/issues", tags=["issues"])



#using the @router decorator and the diffrent methods
@router.get("/issues")
#we can have our function to manage the data
def get_issues():
    return [] 