from importlib import import_module
from pathlib import Path

from naked.core.logger import logger
from naked.core.plugin import Provider

class PluginManager:

    def __init__(self):
        self.providers: list[Provider] = []

    def load(self):
        providers_dir = Path(__file__).parent.parent / "providers"
        logger.info("Loading providers...")

        for folder in providers_dir.iterdir():
            if not folder.is_dir():
                continue

            provider_file = folder / "provider.py"
            if not provider_file.exists():
                continue
            try:
                module = import_module(
                    f"naked.providers.{folder.name}.provider"
                )

            except Exception:
                logger.exception(
                    "Failed to load provider '%s'",
                    folder.name,
                )
                continue

            for obj in module.__dict__.values():
                if (
                    isinstance(obj, type)
                    and issubclass(obj, Provider)
                    and obj is not Provider
                ):
                    instance = obj()
                    if instance.enabled:

                        logger.info(
                            "Loaded provider: %s",
                            instance.name,
                        )
                        self.providers.append(instance)

        logger.info(
            "Loaded %d providers",
            len(self.providers),
        )
        return self.providers