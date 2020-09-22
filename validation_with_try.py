#original
def average(score1, score2, score3):
    first_name = input("What is your first name? ")  # input from user
    last_name = input("What is your last name? ")  # input from user
    age = input("Enter your age: ")  # input from user
    score1, score2, score3 = eval(input("Enter 3 scores separated by a comma: "))  # input from user
    average = (score1 + score2 + score3) / 3  # calculation to add the 3 scores and /3 to generate average score
    print(first_name)  # print user input
    print(last_name)  # print user input
    print(average)  # print calculated average based on user score input

try:
    def average(score1, score2, score3):
        NUMBER_TESTS = 3
        return float((score1 + score2 + score3) / NUMBER_TESTS)
except:
    print("An exception occurred")