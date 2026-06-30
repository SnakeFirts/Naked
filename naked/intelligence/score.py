from naked.intelligence.rules import RULES_BY_PROVIDER
from naked.models.intelligence_score import IntelligenceScore
from naked.models.search_result import SearchResult


class ScoreCalculator:
    """
    Calcula un IntelligenceScore a partir de un SearchResult,
    usando las reglas registradas para ese provider.
    """

    MAX_SCORE = 100

    @classmethod
    def calculate(cls, result: SearchResult) -> IntelligenceScore | None:
        if not result.exists:
            return None

        rules_fn = RULES_BY_PROVIDER.get(result.provider)

        if rules_fn is None:
            # No hay reglas definidas todavía para este provider.
            return None

        applied = rules_fn(result)

        total = sum(points for points, _ in applied)
        total = max(0, min(total, cls.MAX_SCORE))

        reasons = [reason for _, reason in applied]

        return IntelligenceScore(score=total, reasons=reasons)
