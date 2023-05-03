def get_input(question):
    while True:
        user_input = input(question)
        if user_input:
            return user_input
        else:
            print("Please enter a valid input.")

def validate_input(user_input, options):
    if user_input.lower() in options:
        return True
    else:
        return False

print("Welcome to the 30-question form!")

question_number = 1
while question_number <= 30:
    question = f"Question {question_number}: "
    if question_number in [1, 3, 5, 10, 15, 20, 25]:
        user_input = get_input(question)
        if not validate_input(user_input, ["yes", "no"]):
            print("Please enter 'yes' or 'no'.")
            continue
    elif question_number in [2, 4, 6, 11, 16, 21, 26]:
        user_input = get_input(question)
        if not validate_input(user_input, ["a", "b", "c", "d"]):
            print("Please enter 'a', 'b', 'c', or 'd'.")
            continue
    else:
        user_input = get_input(question)

    question_number += 1

print("Thank you for completing the form!")

