"""Class to Test"""


class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(f"{self.question}")

    def new_responses(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print('survey results:')
        for response in self.responses:
            print(f"Language: {response}")


"""question_ = "What language did you first learn to speak?"
survey = AnonymousSurvey(question_)
survey.show_question()
print("Enter q to exit")
while True:
    reply = input("Enter the language: ")
    if reply == 'q':
        break
    survey.new_responses(reply)
print("Thanking you for participating in survey")
survey.show_results()"""

