import unittest
import pygame
import random
from main import create_enemy, create_bonus, WIDTH, HEIGHT  # Імпортуємо функції з основного коду

class TestGame(unittest.TestCase):
    def test_create_enemy(self):
        enemy = create_enemy()

        # Перевіряємо, що список має 3 елементи (поверхня, прямокутник, рух)
        self.assertEqual(len(enemy), 3)

        enemy_surface, enemy_rect, enemy_move = enemy

        # Перевіряємо, що перший елемент - це зображення (Surface)
        self.assertIsInstance(enemy_surface, pygame.Surface)

        # Перевіряємо, що другий елемент - це прямокутник (Rect)
        self.assertIsInstance(enemy_rect, pygame.Rect)

        # Перевіряємо, що третій елемент - це список із двома числами
        self.assertIsInstance(enemy_move, list)
        self.assertEqual(len(enemy_move), 2)
        self.assertIsInstance(enemy_move[0], int)
        self.assertIsInstance(enemy_move[1], int)

        # Перевіряємо, що ворог з'являється на правій межі екрану
        self.assertEqual(enemy_rect.left, WIDTH)

        # Перевіряємо, що ворог з'являється у дозволених межах по Y (50 - HEIGHT - 50)
        self.assertGreaterEqual(enemy_rect.top, 50)
        self.assertLessEqual(enemy_rect.bottom, HEIGHT - 50)

    def test_create_bonus(self):
        bonus = create_bonus()

        # Перевіряємо, що список має 3 елементи
        self.assertEqual(len(bonus), 3)

        bonus_surface, bonus_rect, bonus_move = bonus

        # Перевіряємо, що перший елемент - це зображення (Surface)
        self.assertIsInstance(bonus_surface, pygame.Surface)

        # Перевіряємо, що другий елемент - це прямокутник (Rect)
        self.assertIsInstance(bonus_rect, pygame.Rect)

        # Перевіряємо, що третій елемент - це список із двома числами
        self.assertIsInstance(bonus_move, list)
        self.assertEqual(len(bonus_move), 2)
        self.assertIsInstance(bonus_move[0], int)
        self.assertIsInstance(bonus_move[1], int)

        # Перевіряємо, що бонус з'являється зверху екрану (y = 0)
        self.assertEqual(bonus_rect.top, 0)

        # Перевіряємо, що бонус з'являється у межах відступу по X (50 - WIDTH - 50)
        self.assertGreaterEqual(bonus_rect.left, 50)
        self.assertLessEqual(bonus_rect.right, WIDTH - 50)

if __name__ == '__main__':
    unittest.main()
