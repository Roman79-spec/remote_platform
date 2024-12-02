# Управление платформой онлайн-обучения

## Описание проекта

Данный проект представляет собой систему управления платформой онлайн-обучения. Основная цель проекта — обеспечить удобный способ для пользователей регистрироваться на платформе, выбирать курсы, отслеживать прогресс, проходить модули и завершать курсы.

Код состоит из нескольких классов, каждый из которых отвечает за свою часть функционала:

- `Users` — для управления пользователями (регистрация, выбор курсов, прогресс).
- `Platform` — для управления платформой (регистрация пользователей, добавление и вывод курсов).
- `Courses` — для работы с курсами (добавление модулей, начало и завершение курса).
- `Module` — для управления модулями курсов (начало и завершение модулей).

---

## Основные возможности

### Пользователи:
- Регистрация пользователей на платформе.
- Выбор и прохождение курсов.
- Отслеживание завершённых курсов.
- Просмотр личного прогресса.

### Курсы:
- Добавление новых курсов на платформу.
- Добавление модулей в курсы.
- Обновление статуса курса при завершении модулей.

### Платформа:
- Регистрация пользователей и курсов.
- Вывод списка пользователей и доступных курсов.

---

## Как использовать

### 1. Установка
1. Необходим Python версии 3.8 и выше.
2. Скачайте или клонируйте этот репозиторий
   git clone <URL репозитория>
3. Запустите файл remote_platform.py

### 2. Шаги для работы
1. Зарегистрируйте пользователей с помощью метода user_registrations в классе Platform.
2. Добавьте курсы с помощью метода add_course.
3. Выберите курс для пользователя через метод select_course в классе Users.
4. Начните проходить модули, завершайте их и завершите курс.

### 3. Пример использования
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

## Контакты
email - carltokaize@gmail.com
