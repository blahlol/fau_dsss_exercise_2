import random

def generate_random_integer(range_min, range_max):
    """ 
    Gets a min value and a max value to return a random interger betweent the two values. The values passed as arguments 
    are always converted to integers
    
    Args:
        range_min (int): The starting value of the range
        range_max (int): The stop value of the range

    Returns:
        int: An integer randomly generated from the specified range  
    """
    # generate and return random integer using the random module
    if int(range_min) < int(range_max): return random.randint(int(range_min), int(range_max))

    #in case the larger number of the range is entered as the first argument
    return random.randint(int(range_max),int(range_min)) 


def random_math_operation():
    """
    Radomly chooses one from the following symbols which represent mathematical operations - (+, -, *)

    Returns:
        str: a single character representing a randomly chosen mathematical operation
    """

    #choose one operation from the list of operations 
    return random.choice(['+', '-', '*'])


def perform_math_operation(number_1, number_2, operation):
    """
    Performs the operation specified by the "operation" argument on arguments "number_1" and "number_2"

    Args:
        number_1 (int): The first number involved in the calculation
        number_2 (int): The second number involved in the calculation
        operation (str): a single character representing the operation to be performed

    Returns:
        tuple: a tuple of 2 elements (problem, answer)
            problem (str): of the format "number_1 operation number_2", representing the mathematical problem
            answer (int): the result of performing the operation on the 2 numbers
    """

    #form a string representation of the problem
    problem = f"{number_1} {operation} {number_2}"

    #perform addition if operation is +, subtraction if operation is -, otherwise perform multiplication
    if operation == '+': answer = number_1 + number_2
    elif operation == '-': answer = number_1 - number_2
    else: answer = number_1 * number_2
    return problem, answer

def math_quiz():
    """
    Presents a math quiz containing randomly generated questions/problems to the user.
    The user gets a point for every correct answer.
    The function prints the user score at the end of the quiz.
    """

    #initialization
    score = 0
    total_questions = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        #generate two random integers and the math operation
        number_1 = generate_random_integer(1, 10); number_2 = generate_random_integer(1, 5.5); operation = random_math_operation()

        #solve the problem and prompt the user for their answer
        PROBLEM, ANSWER = perform_math_operation(number_1, number_2, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")

        try:
            useranswer = int(useranswer)
        except:
            print("Invalid input choice. Only integers/numbers are allowed.")

        #increase score by 1 for every correct answer, else display the right answer.
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
