class QuizBrain:

    def __init__(self, p_questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = p_questions_list

    def still_has_questions(self):
        """Check to see if there are still any questions left to serve the user."""
        return self.question_number <= len(self.questions_list) - 1

    def next_question(self):
        """Serves the user the next question."""
        question = self.questions_list[self.question_number]
        self.question_number += 1

        prompt = f"Q.{self.question_number }: {question.text} (True/False)?: "
        answer = self.validate_input(input(prompt), question)
        self.check_answer(answer, question.answer)
        # print(f"Q.{self.question_number }: {question} (True/False)?: ")

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")

    def validate_input(self, user_answer, question):
        """Ensures that the user input is one of the accepted keywords."""
        user_answer = user_answer.lower()
        while user_answer != "true" and user_answer != "false":
            user_answer = input(f"Q.{self.question_number }: {question.text} (True/False)?: ").lower()

        return user_answer
