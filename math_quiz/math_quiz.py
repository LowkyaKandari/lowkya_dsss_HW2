import random

#Selects a random int between min and max
def random_integer(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

#Randomly selects an operator 
def random_operator():
    """
    Random operator from '+', '-', '*'.
    """
    return random.choice(['+', '-', '*'])

#Randomly selected 2 integers and operator is solved
def problem_solution(val_1, val_2, operator):
    """
    Randomly selected two intergers with an operator is solved.
    """
    question = f"{val_1} {operator} {val_2}"
    try:
        if operator == '+': answer = val_1 + val_2
        elif operator == '-': answer = val_1 - val_2
        elif operator == '*': answer = val_1 * val_2
        else: 
            raise ValueError(f"Invalid operation: {operator}")
    except ValueError as e:
        print(f"Error: {e}")
        answer = None # Handle the error by setting 'a' to None
        
    return question, answer

def math_quiz():
    """
    If answer is correct you score a point.
    """
    score = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        int_1 = random_integer(1, 10); int_2 = random_integer(1, 5); operator = random_operator()

        PROBLEM, ANSWER = problem_solution(int_1, int_2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
    math_quiz()
