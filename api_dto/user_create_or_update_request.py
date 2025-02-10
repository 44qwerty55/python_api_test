class UserRequest:

    def __init__(self, name: str, job: str):
        self.__name = name
        self.__job = job

    def get_name(self) -> str:
        return self.__name

    def get_job(self) -> str:
        return self.__job

    def set_name(self, name: str):
        self.__name = name

    def set_job(self, job: str):
        self.__job = job

    def to_dict(self):
        return {
            "name": self.get_name(),
            "job": self.get_job(),
        }