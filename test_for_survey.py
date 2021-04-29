import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def test_question(self):
        question_ = "What language did you first learn to speak?"
        survey = AnonymousSurvey(question_)
        survey.show_question()
        self.assertEqual(survey.question, "What language did you first learn to speak?")

    def test_response(self):
        question_ = "What language did you first learn to speak?"
        survey = AnonymousSurvey(question_)
        survey.new_responses('English')
        self.assertIn('English', survey.responses)

    def test_multiple_responses(self):
        question_ = "What language did you first learn to speak?"
        survey = AnonymousSurvey(question_)
        responses_1 = ['English', 'Telugu', 'Hindi']
        for response in responses_1:
            survey.new_responses(response)
        for response in responses_1:
            self.assertIn(response, survey.responses)


if __name__ == '__main__':
    unittest.main()
