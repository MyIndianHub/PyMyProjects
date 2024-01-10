import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            print(question['question'])
            for i, option in enumerate(question['options'], 1):
                print(f"{i}. {option}")

            user_answer = input("Your answer (enter the option number): ")
            if self.check_answer(question, int(user_answer)):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question['options'][question['correct_option'] - 1]}\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

    def check_answer(self, question, user_answer):
        return user_answer == question['correct_option']

if __name__ == "__main__":
    quiz_questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
            'correct_option': 3
        },
        {
            'question': 'Which programming language is this quiz written in?',
            'options': ['Java', 'Python', 'C++', 'JavaScript'],
            'correct_option': 2
        },
        {
            'question': 'What is the largest mammal in the world?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_option': 2
        },
    ]

    quiz_game = QuizGame(quiz_questions)
    quiz_game.run_quiz()
