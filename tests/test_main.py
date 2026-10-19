import unittest

from main import play


class GuessNumberTests(unittest.TestCase):
    def test_invalid_input_does_not_count(self):
        answers = iter(["abc", "101", "25", "50"])
        messages = []
        result = play(secret=50, input_fn=lambda _: next(answers), output_fn=messages.append)
        self.assertEqual(result, 2)
        self.assertIn("太小了！", messages)

    def test_quit(self):
        self.assertIsNone(play(secret=50, input_fn=lambda _: "q", output_fn=lambda _: None))


if __name__ == "__main__":
    unittest.main()
