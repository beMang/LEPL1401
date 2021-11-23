import unittest
import TurtleBot as tb


class TestTurtleBot(unittest.TestCase):

    t = tb.TurtleBot("tBot")

    def test_init(self):
        self.assertEqual(self.t.angle(), 0,
                         "Your turtleBot is not facing EAST as expected")
        self.assertEqual(self.t.position(), (0, 0),
                         "Your turtleBot is not in 0,0 as expected")

        t_position = tb.TurtleBot("test", 50, 60)
        self.assertEqual(t_position.position(), (50, 60),
                         "Your TurtleBot is not in 50,60 as expected")
        self.assertEqual(self.t.angle(), 0,
                         "Your TurtleBot is not facing EAST as expected")

    def test_turn_left(self):
        expected_position = self.t.position()
        expected_angle = (self.t.angle() + 90) % 360
        self.t.turn_left()
        # below we are using assertAlmostEqual instead if assertEqual to allow for inaccurate calculations
        self.assertAlmostEqual(self.t.angle(
        ), expected_angle, msg="Your turtleBot took a wrong turn or did not update its angle while turning left")
        self.assertEqual(self.t.position(), expected_position,
                         "Your turtleBot changed position while turning left")

    def test_turn_right(self):
        expected_position = self.t.position()
        expected_angle = (self.t.angle() - 90) % 360
        self.t.turn_right()
        self.assertAlmostEqual(self.t.angle(
        ), expected_angle, msg="Your turtleBot took a wrong turn or did not update its angle while turning right")
        self.assertEqual(self.t.position(), expected_position,
                         "Your turtleBot changed position while turning right")

    def test_turn(self):
        expected_position = self.t.position()
        expected_angle = self.t.angle()
        self.t.turn_left()
        self.t.turn_left()
        self.t.turn_right()
        self.t.turn_right()
        self.assertAlmostEqual(self.t.angle(
        ), expected_angle, msg="Your turtleBot took a wrong turn or did not update its angle")
        self.assertEqual(self.t.position(), expected_position,
                         "Your turtleBot changed position while turning")

    def test_move_forward(self):
        forward = 50
        x, y = self.t.position()
        expected_position = (x+forward, 0+y)
        expected_angle = self.t.angle()
        self.t.move_forward(50)
        self.assertEqual(self.t.position(), expected_position,
                         "Your turtleBot has not moved forward "+str(forward)+" as expected")
        self.assertAlmostEqual(self.t.angle(
        ), expected_angle, msg="Your turtleBot changed heading while moving forward")

    def test_movebackward(self):
        backward = 50
        x, y = self.t.position()
        expected_position = (x-backward, y-0)
        expected_angle = self.t.angle()
        self.t.move_backward(50)
        self.assertEqual(self.t.position(), expected_position,
                         "Your turtleBot has not moved backward "+str(backward)+" as expected")
        self.assertAlmostEqual(self.t.angle(
        ), expected_angle, msg="Your turtleBot changed heading while moving backward")

    def test_move(self):
        expected_position = self.t.position()
        expected_angle = self.t.angle()
        self.t.move_forward(50)
        self.t.move_backward(10)
        self.t.move_backward(90)
        self.t.move_forward(50)
        self.assertAlmostEqual(self.t.angle(
        ), expected_angle, msg="Your turtleBot took a wrong turn or did not update its angle")
        self.assertEqual(self.t.position(), expected_position,
                         "Your turtleBot changed position while turning")

        def test_unplay(self):
            expected_position = (0, 0)
            self.t.unplay()
            # On s'assure que l'historique est vide
            self.assertEqual(self.t.history(), [],
                            "L'historique n'a pas été vidé correctement")
            # Et qu'on est bien revenu à l'endroit de base
            self.assertEqual(self.t.position(), expected_position,
                            "Le bot n'est pas revenu à la position initiale comme prévu")

    def test_history(self):
        self.t.move_backward(50)
        self.t.move_forward(600)
        self.t.turn_right()
        self.t.turn_left()
        expected_history = [("backward", 50), ("forward",
                                               600), ("right", 90), ("left", 90)]
        self.assertEqual(self.t.history(), expected_history,
                         "L'historique n'est pas celui qui est attendu")
        self.t.unplay()  # Pour revenir à la place normales


if __name__ == '__main__':
    unittest.main(verbosity=2)
