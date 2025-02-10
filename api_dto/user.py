class User:

    def __init__(self, id: int, email: str, first_name: str, last_name: str, avatar: str):
        self.__id = id
        self.__email = email
        self.__first_name = first_name
        self.__last_name = last_name
        self.__avatar = avatar

    def get_id(self) -> int:
        return self.__id

    def get_email(self) -> str:
        return self.__email

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_avatar(self) -> str:
        return self.__avatar

    def set_id(self, id: int):
        self.__id = id

    def set_email(self, email: str):
        self.__email = email

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def set_avatar(self, avatar: str):
        self.__avatar = avatar

    def to_dict(self):
        return {
            "id": self.get_id(),
            "email": self.get_email(),
            "first_name": self.get_first_name(),
            "last_name": self.get_last_name(),
            "avatar": self.get_avatar()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            avatar=data.get('avatar')
        )