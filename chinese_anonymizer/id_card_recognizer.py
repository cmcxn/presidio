from presidio_analyzer import Pattern, PatternRecognizer

class ChineseIdCardRecognizer(PatternRecognizer):
    def __init__(self):
        id_card_patterns = [
            Pattern(
                name="id_card",
                regex=r"\b[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]\b",
                score=0.95
            )
        ]
        super().__init__(
            supported_entity="ID_CARD",
            patterns=id_card_patterns,
            supported_language="zh"
        )