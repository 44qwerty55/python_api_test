from api_dto.user_create_or_update_request import UserRequest


class UserUpdateResponse:

    def __init__(self, name: str, job: str, updated_at: str=None):
        self.__name = name
        self.__job = job
        self.__updated_at = updated_at

    def get_name(self) -> str:
        return self.__name

    def get_job(self) -> str:
        return self.__job

    def get_updated_at(self) -> str:
        return self.__updated_at

    def set_name(self, name: str):
        self.__name = name

    def set_job(self, job: str):
        self.__job = job

    def set_updated_at(self, updated_at: str):
        self.__updated_at = updated_at

    def to_dict(self):
        return {
            "name": self.get_name(),
            "job": self.get_job(),
            "updatedAt": self.get_updated_at()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            job=data.get('job'),
            updated_at=data.get('updatedAt'),
        )

    @classmethod
    def instance(cls, request: UserRequest, update_date: str):
        return cls(
            name=request.get_name(),
            job=request.get_job(),
            updated_at=update_date
        )