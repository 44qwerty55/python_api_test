from api_dto.support import Support
from api_dto.user import User


class UserResponse:

    def __init__(self, data: User, support: Support):
        self.__user = data
        self.__support = support

    def get_user(self) -> User:
        return self.__user

    def get_support(self) -> Support:
        return self.__support

    def to_dict(self):
        return {
            "data": self.get_user().to_dict(),
            "support": self.get_support().to_dict()
        }

    @classmethod
    def from_json(cls, json_data):
        user_objects = User.from_dict(json_data.get('data'))
        support_object = Support.from_dict(json_data.get('support'))

        return cls(
            data=user_objects,
            support=support_object
        )