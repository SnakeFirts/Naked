from abc import ABC, abstractmethod

from naked.models.search_result import SearchResult

class Provider(ABC):
    name: str = "provider"
    enabled: bool = True

    @abstractmethod
    async def search(self, username: str) -> SearchResult:
        pass