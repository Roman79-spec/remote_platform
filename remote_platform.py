class Users:
    def __init__(self, first_name, last_name, login, password):
        """Инициализация атрибутов"""
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.progress = 0
        self.personal_course = []
        self.history_complete_course = []
    
    def __str__(self):
        """Строковый метод для вывода информации о пользователе"""
        return f'Имя: {self.first_name}. Фамилия: {self.last_name}.\nЛогин: {self.login}. Пароль: {self.password}.'
    
    def select_course(self, course):
        """Выбор курса"""
        print(f'\nПопытка выбрать курс: {course.course_name}')
        if course.course_name not in self.personal_course:
            print(f'Курс {course.course_name} выбран успешно!')
            self.personal_course.append(course)
        else:
            print('\nНельзя выбрать один и тот же курс!')
    
    def print_select_courses(self):
        """Вывод выбранных курсов"""
        print(f'\nВыбранные курсы: ')
        for course in self.personal_course:
            print(f'Курс: {course.course_name}. Статус: {course.status}')

    def print_history_complete_courses(self):
        """Вывод списка завершенных курсов"""
        if self.history_complete_course:
            print('Завершенные курсы: ')
            for course in self.history_complete_course:
                print(course.course_name)        
        else:
            print('Вы еще не прошли курс!')
    
    def show_progress(self):
        """Вывод прогресса пользователя"""
        print(f'\nПрогресс пользователя {self.first_name} {self.last_name}')
        if not self.personal_course:
            print('Еще ни одного курса не выбрано!')

        for course in self.personal_course:
            print(f'Курс {course.course_name}. Прогресс: {course.progress}. Статус {course.status}.')

class Platform:
    def __init__(self):
        """Инициализация атрбиутов"""
        self.all_users = {}
        self.course_list = {}

    def user_registrations(self, identifer_user, user):
        """Регистрация пользователей"""
        if identifer_user not in self.all_users:
            self.all_users[identifer_user] = user
        else:
            print('Такой пользователь уже существует!')
        
    def print_users(self):
        """Вывод все курсов"""
        print('Список всех пользователей: ')
        for user in self.all_users.values():
            print(user)

    def add_course(self, identifier_course, course):
        """Добавление курса на платформу"""
        self.course_list[identifier_course] = course

    def print_courses(self):
        """Вывод всех курсов"""
        if self.course_list:
            print(f'Список доступных курсов: ')
            for course in self.course_list.values():
                print(course)
        else:
            print('\nНи одного курса не добавлено!')