import unittest
from remote_platform import Users, Platform, Courses, Module

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

        self.module1 = Module('Модуль 1')
        self.module2 = Module('Модуль 2')
        self.module3 = Module('Модуль 3')
        

         

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

    def test_status_course(self):
        """Проверка на вывод правильного курса"""
        self.user1.select_course(self.course1)
        self.platform.add_course('Курс 1', self.course1)
        self.course1.course_started(self.course1, self.user1)

        self.module1.start_module()
        self.module1.complete_module(self.course1)
        self.user1.show_progress()
        self.module2.start_module()
        self.module2.complete_module(self.course1)
        self.user1.show_progress()
        self.module3.start_module()
        self.module3.complete_module(self.course1)
        self.user1.show_progress()
        self.course1.complete_course(self.user1) 
        self.assertEqual(self.course1.status, self.course1.COMPLETE)
        


        
        

if __name__ == '__main__':
    unittest.main()
        


