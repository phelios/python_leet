from unittest import TestCase

from problems.robot_obstacle import RobotObstacle


class TestRobotObstacle(TestCase):
    def test_solve(self):
        grid = [[1, 1, 1],
                [1, 0, 1],
                [0, 9, 1]]

        self.assertEqual(3, RobotObstacle().solve(grid))

