import unittest
from remote_platform import Users, Platform, Courses 

class TestUsers(unittest.TestCase):
    def setUp(self):
        """Создание объектов 1 раз, чтобы юзать каждый раз"""
        self.user1 = Users('Боня', 'Бобикова', 'bonya_bobik', '123456789')
        self.user2 = Users('Бобик', 'Собачкин', 'bobik_sobachkin', '124567')
        self.user3 = Users('Барсик', 'Барсиков', 'barsik_barsikov', 'q1q2q3q4q5')

        self.platform = Platform()
        
        self.course1 = Courses('Основы программирования на Python', 'Programming')
        self.course2 = Courses('Основы программирования на JS', 'Programming')
        self.course3 = Courses('Математика. Продвинутый уровень', 'Educations')

    def test_add_user(self):
        """Проверка что пользователь находится в словаре"""
        #Добавляем
        self.platform.user_registrations('Пользователь 1', self.user1)
        self.platform.user_registrations('Пользователь 2', self.user2)
        self.platform.user_registrations('Пользователь 3', self.user3)
        #Проверяем
        self.assertIn('Пользователь 1', self.platform.all_users)
        self.assertIn('Пользователь 2', self.platform.all_users)
        self.assertIn('Пользователь 3', self.platform.all_users)

        self.assertIn(self.user1, self.platform.all_users.values())
        self.assertIn(self.user2, self.platform.all_users.values())
        self.assertIn(self.user3, self.platform.all_users.values())
        #Проверяем ТОЛЬКО объекты, что они соответсвуют добавленным пользователям
        self.assertEqual(self.platform.all_users['Пользователь 1'], self.user1)
        self.assertEqual(self.platform.all_users['Пользователь 2'], self.user2)
        self.assertEqual(self.platform.all_users['Пользователь 3'], self.user3)

    def test_add_courses(self):
        pass


if __name__ == '__main__':
    unittest.main()
        


