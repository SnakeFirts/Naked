from naked.models.profiles.base import BaseProfile

class InstagramProfile(BaseProfile):

    followers: int | None = None

    following: int | None = None

    posts: int | None = None

    verified: bool = False

    private: bool = False