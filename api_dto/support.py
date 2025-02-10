class Support:

    def __init__(self, url: str, text: str):
        self.__url = url
        self.__text = text

    def get_url(self) -> str:
        return self.__url

    def get_text(self) -> str:
        return self.__text

    def set_url(self, url: str):
        self.__url = url

    def set_text(self, text: str):
        self.__text = text

    def to_dict(self):
        return {
            "url": self.get_url(),
            "text": self.get_text()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            url=data.get('url'),
            text=data.get('text')
        )

