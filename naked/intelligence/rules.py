"""
Reglas de puntuación por provider.

Cada función recibe el SearchResult ya construido (con exists=True)
y devuelve una lista de tuplas (puntos, motivo).

Mantener las reglas aquí, separadas del calculador, permite añadir
providers nuevos sin tocar la lógica de cálculo.
"""

from naked.models.search_result import SearchResult


def github_rules(result: SearchResult) -> list[tuple[int, str]]:
    rules: list[tuple[int, str]] = []

    # Toda la info viene de la API oficial de GitHub, no de scraping.
    rules.append((40, "Official API"))

    if result.username and result.profile:
        # GitHub API ya filtra por username exacto en la URL,
        # así que si hubo "exists=True" el match es exacto.
        rules.append((20, "Username exact match"))

    if result.profile is not None:
        rules.append((20, "Public profile"))

    if result.url:
        rules.append((20, "Profile URL verified"))

    return rules


RULES_BY_PROVIDER = {
    "github": github_rules,
}
