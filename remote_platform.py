class Users:
    """Класс для управления пользователями"""
    def __init__(self, first_name: str, last_name: str, login: str, password: str)-> None:
        """Инициализация атрибутов"""
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.login: str = login
        self.password: str = password
        self.progress: int = 0
        self.personal_course: list = []
        self.history_complete_course: list = []
    
    def __str__(self) -> None:
        """Строковый метод для вывода информации о пользователе"""
        return (f'Имя: {self.first_name}. Фамилия: {self.last_name}.\n'
                f'Логин: {self.login}. Пароль: {self.password}.')
    
    def select_course(self, course: 'Courses')-> None:
        """Выбор курса"""
        print(f'\nПопытка выбрать курс: {course.course_name}')
        if course.course_name not in self.personal_course:
            print(f'Курс {course.course_name} выбран успешно!')
            self.personal_course.append(course)
        else:
            print('\nНельзя выбрать один и тот же курс!')
    
    def print_select_courses(self)-> None:
        """Вывод выбранных курсов"""
        print('\nВыбранные курсы: ')
        for course in self.personal_course:
            print(f'Курс: {course.course_name}. Статус: {course.status}')

    def print_history_complete_courses(self)-> None:
        """Вывод списка завершенных курсов"""
        if self.history_complete_course:
            print('Завершенные курсы: ')
            for course in self.history_complete_course:
                print(course.course_name)        
        else:
            print('Вы еще не прошли курс!')
    
    def show_progress(self)-> None:
        """Вывод прогресса пользователя"""
        print(f'\nПрогресс пользователя {self.first_name} {self.last_name}')
        if not self.personal_course:
            print('Еще ни одного курса не выбрано!')
        for course in self.personal_course:
            print(f'Курс {course.course_name}. Прогресс: {course.progress}.\n'
                  f'Статус {course.status}.')

class Platform:
    """Для управления и добавление курсов"""
    def __init__(self)-> None:
        """Инициализация атрбиутов"""
        self.all_users: dict = {}
        self.course_list: dict = {}

    def user_registrations(self, identifer_user: str, user: 'Users')-> None:
        """Регистрация пользователей"""
        if identifer_user not in self.all_users:
            self.all_users[identifer_user] = user
        else:
            print('Такой пользователь уже существует!')
        
    def print_users(self)-> None:
        """Вывод все курсов"""
        print('Список всех пользователей: ')
        for user in self.all_users.values():
            print(user)

    def add_course(self, identifier_course: str, course: 'Courses')-> None:
        """Добавление курса на платформу"""
        self.course_list[identifier_course] = course

    def print_courses(self)-> None:
        """Вывод всех курсов"""
        if self.course_list:
            print('Список доступных курсов: ')
            for course in self.course_list.values():
                print(course)
        else:
            print('\nНи одного курса не добавлено!')
            
class Courses:
    """Для управления курсами"""
    NOT_STARTED = 'not started'
    IN_PROGRESS = 'in progress'
    COMPLETE = 'complete'
    def __init__(self, course_name: str, direction_course: str)-> None:
        """Инициализация атрибутов"""
        self.course_name: str = course_name
        self.direction_course: str = direction_course
        self.modules: list = []
        self.status: str = Courses.NOT_STARTED
        self.progress: int = 0

    def __str__(self)-> None:
        """Строковый метод"""
        return f'Название: {self.course_name}. Направление: {self.direction_course}.'
    
    def add_module(self, module: str)-> None:
        "Добавление модуля"
        if module not in self.modules:
            self.modules.append(module)
        else:
            print('Модуль уже добавлен!')
            print('Модуль уже добавлен!')


    def course_started(self, course: 'Courses', user:'Users')-> None:
        """Начало курса"""
        if course.status == Courses.NOT_STARTED:
            if course in user.personal_course:
                course.status = Courses.IN_PROGRESS
                print(f'\nКурс {course.course_name} начат! Успехов!')
            else:
                print(f'Нельзя начать курс {course.course_name}, он не выбран вами!')
        else:
            print(f'Курс {course.course_name} уже начат!')

    def course_update(self)-> None:
        """Обновление курса и прогресс"""
        if self.status == Courses.IN_PROGRESS:
            complete_module = sum(1 for module in self.modules if module.status == Courses.COMPLETE)
            if len(self.modules) > 0:
                self.progress = round(complete_module / len(self.modules) * 100)
            else:
                self.progress = 0
        else:
            print('Начните проходить курс!')

    def complete_course(self, user: Users)-> None:
        """Завершаем курс"""
        if self.progress == 100:
            self.status = Courses.COMPLETE
            print('Вы завершили курс. Поздравляем!\n')
            user.personal_course.remove(self)
            user.history_complete_course.append(self)
        else:
            print('Курс еще не пройден! Завершите все модули!')

            
class Module:
    "Для управления модулями"
    NOT_STARTED = 'not started'
    IN_PROGRESS = 'in progress'
    COMPLETE = 'complete'
    def __init__(self, title: str)-> None:
        """Инициализация атрибутов"""
        self.title: str = title
        self.status: str = Module.NOT_STARTED
        self.progress: int = 0
    
    def start_module(self)-> None:
        """Начинаем модуль"""
        self.status = Module.IN_PROGRESS
        
    def complete_module(self, course: 'Courses')-> None:
        """Завершаем модуль"""
        if self.status == Module.IN_PROGRESS:
            self.status = Module.COMPLETE
            self.progress = 100
            course.course_update()
            print('Поздравляем над завершением модуля!')
        else:
            print('Невозможно завершить модуль. Начните его прохождение!')

user1 = Users('Боня', 'Бобикова', 'bonya_bobik', '123456789')
user2 = Users('Бобик', 'Собачкин', 'bobik_sobachkin', '124567')
user3 = Users('Барсик', 'Барсиков', 'barsik_barsikov', 'q1q2q3q4q5')

platform = Platform()
platform.user_registrations('Пользователь1', user1)
platform.user_registrations('Пользователь2', user2)
platform.user_registrations('Пользователь3', user3)

course1 = Courses('Основы программирования на Python', 'Programming')
course2 = Courses('Основы программирования на JS', 'Programming')
course3 = Courses('Математика. Продвинутый уровень', 'Educations')

module1 = Module('Модуль 1')
module2 = Module('Модуль 2')
module3 = Module('Модуль 3')

platform.add_course('Курс 1', course1)
platform.add_course('Курс 2', course2)
platform.add_course('Курс 3', course3)

course1.add_module(module1)
course1.add_module(module2)
course1.add_module(module3)

platform.print_courses()


user1.select_course(course1)
user1.print_select_courses()



platform.add_course('Курс 1', course1)
platform.add_course('Курс 2', course2)
platform.add_course('Курс 3', course3)


course1.course_started(course1, user1)

module1.start_module()

module1.complete_module(course1)
user1.show_progress()

module2.start_module()
module2.complete_module(course1)

user1.show_progress()
module3.start_module()

module3.complete_module(course1)
user1.show_progress()

course1.course_update()
course1.complete_course(user1)



user1.print_history_complete_courses()
