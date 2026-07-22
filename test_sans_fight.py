import unittest
import pygame

from sans_fight import SansFight


class SansFightTests(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.surface = pygame.Surface((640, 480))
        self.fight = SansFight(self.surface)

    def test_start_sets_active_and_resets(self):
        self.fight.start()
        self.assertTrue(self.fight.active)
        self.assertEqual(self.fight.state, "intro")

    def test_update_does_not_crash(self):
        self.fight.start()
        self.fight.update(0.016, [])
        self.assertTrue(self.fight.active)


if __name__ == "__main__":
    unittest.main()
