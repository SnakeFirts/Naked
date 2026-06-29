import asyncio

from naked.core.logger import logger
from naked.core.plugin import Provider
from naked.models.search_result import SearchResult

class NakedEngine:

    def __init__(self, providers: list[Provider]):
        self.providers = providers

    async def search(self, username: str) -> list[SearchResult]:
        logger.info("Searching '%s'...", username)

        tasks = [
            provider.search(username)
            for provider in self.providers
        ]

        results = await asyncio.gather(
            *tasks,
            return_exceptions=True,
        )

        valid_results = []
        for result in results:
            if isinstance(result, Exception):
                logger.exception(result)
                continue
            valid_results.append(result)

        logger.info(
            "Search completed (%d results)",
            len(valid_results),
        )

        return valid_results