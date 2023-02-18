class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current_question.prompt} (True/False): ")
        self.check_answer(choice, current_question)

    def still_has_question(self):
        return int(self.question_number) < int(len(self.question_list))

    def check_answer(self, choice, current_question):
        if choice.lower() == current_question.prompt_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong.")
        print(f"The correct answer was {current_question.prompt_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")

    def print_final_score(self):
        print(f"Your final score is {self.score}/{self.question_number}")
