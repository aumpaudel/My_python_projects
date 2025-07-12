from  random import shuffle
user = input("Enter your name: ")
print("Please answer the following questions by selecting the correct option.")
print(f"Welcome {user} to the quiz!")
class quiz():
    @staticmethod
    def q1():
        try:
            print("Q. What is the output of print(2 ** 3)?")
            print("a) 6")
            print("b) 8")                                    #✅
            print("c) 9")
            print("d) 5") 
            answer = input("Enter your answer (a, b, c, d): ")
            if answer.lower() == 'b':
                print("Correct✅!")
                return 1
            else:
                print(f"Incorrect❌. The correct answer is b) 8.")
                return 0
        except Exception as e:
            print(f"An error occurred❌: {e}")
            return 0
    @staticmethod
    def q2():
        try:
            print("Q. Which keyword is used to define a function in Python?")
            print("a) func")
            print("b) define")
            print("c) def")                                                 #✅
            print("d) function")
            answer = input("Enter your answer (a, b, c, d): ")
            if answer.lower() == 'c':
                print("Correct✅!")
                return 1
            else:
                print(f"Incorrect❌. The correct answer is c) def.")
                return 0
        except Exception as e:
            print(f"An error occurred❌: {e}")
            return 0
    @staticmethod
    def q3():
        try:
            print("Q. What will type([]) return?")
            print("a) <class 'list'>")                                          #✅
            print("b) <class 'dict'>")
            print("c) <class 'tuple'>")
            print("d) <class 'set'>")
            answer = input("Enter your answer (a, b, c, d): ")
            if answer.lower() == 'a':
                print("Correct✅!")
                return 1
            else:
                print(f"Incorrect❌. The correct answer is a) <class 'list'>.")
                return 0
        except Exception as e:
            print(f"An error occurred❌: {e}")
            return 0
    @staticmethod
    def q4():
        try:
            print("Q. Which of the following is immutable?")
            print("a) list")
            print("b) set")
            print("c) tuple")                                                #✅
            print("d) dictionary")
            answer = input("Enter your answer (a, b, c, d): ")
            if answer.lower() == 'c':
                print("Correct✅!")
                return 1
            else:
                print(f"Incorrect❌. The correct answer is c) tuple.")
                return 0
        except Exception as e:
            print(f"An error occurred❌: {e}")
            return 0
    @staticmethod
    def q5():
        try:
            print("Q. What is the value of (7 × 8) − (6 × 9)?")
            print("a) 2")                                                    #✅
            print("b) 4")
            print("c) −2")
            print("d) −4")
            answer = input("Enter your answer (a, b, c, d): ")
            if answer.lower() == 'a':
                print("Correct✅!")
                return 1
            else:
                print(f"Incorrect❌. The correct answer is a) 2.")
                return 0
        except Exception as e:
            print(f"An error occurred❌: {e}")
            return 0
    @staticmethod
    def q6():
        try:
            print("Q. What is the next prime number after 11?")
            print("a) 12")
            print("b) 13  ")                                     #✅
            print("c) 15")
            print("d) 17")
            answer = input("Enter your answer (a, b, c, d): ")
            if answer.lower() == 'b':
                print("Correct✅!")
                return 1
            else:
                print(f"Incorrect❌. The correct answer is b) 13.")
                return 0
        except Exception as e:
            print(f"An error occurred❌: {e}")
            return 0
    @staticmethod
    def q7():
        try:
            print("Q. The sum of the angles in any triangle is:")
            print("a) 90°")
            print("b) 180° ")                                    # ✅
            print("c) 270°")
            print("d) 360°")
            answer = input("Enter your answer (a, b, c, d): ")
            if answer.lower() == 'b':
                print("Correct✅!")
                return 1
            else:
                print(f"Incorrect❌. The correct answer is b) 180°.")
                return 0
        except Exception as e:
            print(f"An error occurred❌: {e}")
            return 0
questions = [quiz.q1,quiz.q2,quiz.q3,quiz.q4,quiz.q5,quiz.q6,quiz.q7]
shuffle(questions)
score = 0
for q in questions:
    score += q()
print("\nQuiz completed! 🎉")
print(f"Thank you {user} for answering the questions!")
print("You have completed the quiz.")
print("Here are your results:")
if score >= 5:
    print("Great job! 🎉")
else:
    print("Nice try! Keep practicing! 👍")
print(f"Your total score is: {score} out of 7")