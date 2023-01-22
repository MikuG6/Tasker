import requests

# class Project(object):
#     def __init__(self, number, two_number):
#         self.number = number
#
#     def create(self, *args):
#         self.args = args
#
#     @classmethod
#     def from_file(cls, some_file):
#         with open(some_file, "r") as f:
#             data = f.read()
#         return cls(data)
#
#     # @staticmethod
#     def calc(self, one, two):
#         return one + two + self.number
#
#
# proj = Project(1)
# proj.calc(1, 2)  # 4
# Project.calc(proj, 1, 2)  # 4
# Project.create_with_1()
# Project(1)
# proj2 = Project.from_file("some_file.txt")

DOMAIN = 'localhost:8000'


class NonAuthorized(Exception):
    pass


class InheritLogic(object):
    @staticmethod
    def _authenticate(username, password):
        requests.post(f"{DOMAIN}/auth", data={
            "username": username,
            "password": password
        })

    @staticmethod
    def add_user(username, password, password2):
        if password != password2:
            raise ValueError
        # user = User.objects.create(username=username, password=password)
        # return user
        return None


class ConsoleClient(InheritLogic):
    def run(self):
        while True:
            try:
                self.auth()
            except Exception:
                print("Некорректные данные")

    def auth(self):
        response = input("1) Вход\n"
                         "2) Регистрация"
                         "3) Выход")
        if response == "1":
            self.sign_in()
        elif response == "2":
            self.sign_up()
        elif response == "3":
            self.sign_out()
        else:
            raise ValueError("Некорректный ответ")

    def sign_in(self):  # Вход
        username = input("Введите логин")
        password = input("Введите пароль")
        user = self._authenticate(username, password)
        self.show_menu()

    def sign_up(self):  # Регистрация
        username = input("Введите логин")
        password = input("Введите пароль")
        password2 = input("Введите подтверждение пароля")
        self._authenticate(username, password, password2)

    def sign_out(self):  # Выход
        exit()

    def show_menu(self, user):
        tasks_pretty = '\n\t'.join([f"[{task.id}] {task.title}" for task in user.tasks.all()])
        print("Tasks:\n"
              f"\t{tasks_pretty or 'No tasks'}")
        response = input("1) Создать задачу"
                         "2) Выбрать задачу")
        if response == "1":
            self.create_task()
        elif response == "2":
            self.choice_task()
        else:
            raise ValueError("Некорректный ответ")

    def create_task(self):
        pass

    def choice_task(self):
        pass


if __name__ == '__main__':
    ConsoleClient().run()
