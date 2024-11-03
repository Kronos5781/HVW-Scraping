from pydantic import BaseModel


class Report(BaseModel):
    content: str
