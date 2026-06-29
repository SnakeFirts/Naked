from naked.core.plugin import Provider
from naked.models.search_result import SearchResult

class DummyProvider(Provider):
    name = "dummy"

    async def search(self, username: str) -> SearchResult:
        return SearchResult(
            provider=self.name,
            username=username,
            exists=True,
            url=f"https://dummy.local/{username}",
            
            metadata={
                "message": "Dummy provider works!"
            }
        )