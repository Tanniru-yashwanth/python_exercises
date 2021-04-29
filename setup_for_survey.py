
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question_ = "What language did you first learn to speak?"
        self.survey = AnonymousSurvey(question_)
        self.responses_1 = ['English', 'Telugu', 'Hindi']

    def test_question(self):
        self.survey.show_question()
        self.assertEqual(self.survey.question, "What language did you first learn to speak?")

    def test_single_response(self):
        self.survey.new_responses(self.responses_1[0])
        self.assertIn(self.responses_1[0], self.survey.responses)

    def test_multiple_responses(self):
        for response in self.responses_1:
            self.survey.new_responses(response)
        for response in self.responses_1:
            self.assertIn(response, self.survey.responses)


if __name__ == '__main__':
    unittest.main()
