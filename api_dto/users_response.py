from api_dto.support import Support
from api_dto.user import User
import json


class UsersResponse:
    def __init__(self, page: int, per_page: int, total: int, total_pages: int, data: [User], support: Support):
        self.__page = page
        self.__per_page = per_page
        self.__total = total
        self.__total_pages = total_pages
        self.__data = data
        self.__support = support

    def get_page(self) -> int:
        return self.__page

    def get_per_page(self) -> int:
        return self.__per_page

    def get_total(self) -> int:
        return self.__total

    def get_total_pages(self) -> int:
        return self.__total_pages

    def get_user(self) -> [User]:
        return self.__data

    def get_support(self) -> Support:
        return self.__support

    def to_dict(self):
        return {
            "page": self.get_page(),
            "per_page": self.get_per_page(),
            "total": self.get_total(),
            "total_pages": self.get_total_pages(),
            "data": [user.to_dict() for user in self.get_user()],
            "support": self.get_support().to_dict()
        }

    @classmethod
    def from_json(cls, json_data):
        user_objects = [User.from_dict(user) for user in json_data.get('data', [])]
        support_object = Support.from_dict(json_data.get('support'))

        return cls(
            page=json_data.get('page'),
            per_page=json_data.get('per_page'),
            total=json_data.get('total'),
            total_pages=json_data.get('total_pages'),
            data=user_objects,
            support=support_object
        )