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
