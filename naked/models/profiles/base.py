from pydantic import BaseModel

class BaseProfile(BaseModel):
    """
    Información común a cualquier red social.
    """

    display_name: str | None = None

    avatar_url: str | None = None

    bio: str | None = None

    location: str | None = None

    website: str | None = None