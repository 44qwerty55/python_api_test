from api_dto.user_create_or_update_request import UserRequest


class UserCreateResponse:

    def __init__(self, name: str, job: str, id: int=None, create_at: str=None):
        self.__name = name
        self.__job = job
        self.__id = id
        self.__create_at = create_at

    def get_name(self) -> str:
        return self.__name

    def get_job(self) -> str:
        return self.__job

    def get_id(self) -> int:
        return self.__id

    def get_create_at(self) -> str:
        return self.__create_at

    def set_name(self, name: str):
        self.__name = name

    def set_job(self, job: str):
        self.__job = job

    def set_id(self, id: int):
        self.__id = id

    def set_create_at(self, create_at: str):
        self.__create_at = create_at

    def to_dict(self):
        return {
            "name": self.get_name(),
            "job": self.get_job(),
            "id": self.get_id(),
            "createAt": self.get_create_at()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            job=data.get('job'),
            id=data.get('id'),
            create_at=data.get('createAt'),
        )

    @classmethod
    def instance(cls, request: UserRequest, id: int, create_date: str):
        return cls(
            name=request.get_name(),
            job=request.get_job(),
            id=id,
            create_at=create_date
        )