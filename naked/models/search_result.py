from typing import Any

from pydantic import BaseModel

from naked.models.profiles.base import BaseProfile


class SearchResult(BaseModel):

    provider: str

    username: str

    exists: bool

    url: str | None = None

    profile: BaseProfile | None = None

    raw: dict[str, Any] | None = None