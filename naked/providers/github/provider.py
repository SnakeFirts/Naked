import httpx

from naked.core.plugin import Provider
from naked.intelligence.score import ScoreCalculator
from naked.models.profiles.github import GithubProfile
from naked.models.search_result import SearchResult
from typing import Any

class GithubProvider(Provider):
    name = "github"

    API_URL = "https://api.github.com/users"

    async def search(self, username: str) -> SearchResult:
        data = await self._fetch_user(username)
        return self._build_result(username, data)

    async def _fetch_user(self, username: str) -> dict[str, Any] | None:
        """Obtiene la información del usuario desde la API."""

        url = f"{self.API_URL}/{username}"
            
        headers = {
            "User-Agent": "NAKED/2.0"
        }

        async with httpx.AsyncClient(
            timeout=10,
            headers=headers,
        ) as client:
            response = await client.get(url)

        if response.status_code == 404:
            return None

        response.raise_for_status()

        return response.json()

    def _build_profile(self, data: dict[str, Any]) -> GithubProfile:
        """Convierte la respuesta de GitHub en un GithubProfile."""

        return GithubProfile(
            display_name=data.get("name"),
            avatar_url=data.get("avatar_url"),
            bio=data.get("bio"),
            company=data.get("company"),
            location=data.get("location"),
            website=data.get("blog"),
            followers=data.get("followers"),
            following=data.get("following"),
            repositories=data.get("public_repos"),
        )
        
    def _build_result(
        self,
        username: str,
        data: dict[str, Any] | None,
    ) -> SearchResult:

        if data is None:
            return SearchResult(
                provider=self.name,
                username=username,
                exists=False,
                url=f"https://github.com/{username}",
            )

        profile = self._build_profile(data)

        result = SearchResult(
            provider=self.name,
            username=username,
            exists=True,
            url=data.get("html_url"),
            profile=profile,
            raw=data,
        )

        result.score = ScoreCalculator.calculate(result)

        return result