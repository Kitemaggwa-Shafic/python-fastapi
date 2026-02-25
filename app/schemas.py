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
  