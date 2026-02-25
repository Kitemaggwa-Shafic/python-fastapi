# using pydantic to map our data for issues and resources
# like post request we send issues with body title, desc etc, for update too
# also for getting data back from db
# setting strict rules for data issues

from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low"
    high = "high"
    critical="critical"


#schema for creating an issue
class IssueCreate(BaseModel):
    title: str = Field(min_legth=3, max_legth=100) 
    description: str = Field(min_length=3, max_length=500)
    priority: IssuePriority = IssuePriority.low 

#updating an issue
class UpdateIssue(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_legth=500)
    priority: Optional[IssuePriority] = None
    status: Optional[IssueStatus] = None

# schema for response after getting back all issue data from DB
class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    priority: IssuePriority
    status: IssueStatus