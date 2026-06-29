from naked.models.profiles.base import BaseProfile

class GithubProfile(BaseProfile):

    followers: int | None = None

    following: int | None = None

    repositories: int | None = None

    company: str | None = None