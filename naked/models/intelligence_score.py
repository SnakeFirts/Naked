from pydantic import BaseModel


class IntelligenceScore(BaseModel):
    score: int
    reasons: list[str]
