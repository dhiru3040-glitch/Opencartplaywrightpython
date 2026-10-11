from faker import Faker


class RandomDataUtil:
    def __init__(self, page=None):
        self.page = page
        self.faker = Faker()

    def get_first_name(self) -> str:
        return self.faker.first_name()

    def get_last_name(self) -> str:
        return self.faker.last_name()

    def get_full_name(self) -> str:
        return self.faker.name()

    def get_email(self) -> str:
        return self.faker.email()

    def get_phone_number(self) -> str:
        return self.faker.phone_number()

    def get_username(self) -> str:
        return self.faker.user_name()

    def get_password(self, length: int = 10) -> str:
        return self.faker.password(length=length)
