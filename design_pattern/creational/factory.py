class GreekLocalizer:
    """A simple localizer a la gettext"""

    def __init__(self) -> None:
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg: str) -> str:
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply echoes the message"""

    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") -> object:
    """Factory"""
    localizers = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }

    return localizers[language]()


if __name__ == "__main__":
    e, g = get_localizer(language="English"), get_localizer(language="Greek")
    for msg in "dog parrot cat bear".split():
        print(e.localize(msg), g.localize(msg))
