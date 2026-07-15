# | 10 | ❓ Quiz Application        | Lists, dictionaries, scoring, loops       |

from data import python_questions, gk_questions, cs_questions
from random import randint

name = ""
category = 0
correct_score = 0
wrong_score = 0

#this fuction greeth the user and take name and choice as input and store it in global variables.
def wellcome():     
    #print the logo and greet user    
    print('''       
 ____        _
|  _ \ _   _(_)_ __
| |_) | | | | | '_ \
|  __/| |_| | | | | |
|_|    \__, |_|_| |_|
       |___/    
          
wellcome to the quiz      

''')
    #take input from the user and stores it in global variable "name"
    global name
    name = input("Enter your name :- ")

    #print a available option 
    print(f"""
Choose category {name}
1. Python
2. General Knowledge
3. Computer Science
          """)
    
    #take input of user choice and save it in global choice variable.
    global choice
    choice = int(input("Enter your choice :- "))


#this fuction display question, options and compare is the answer is correct or not 
#this works with python questions
def display_py_questions():
    random = int(randint(0,49))         #generate a randome number 
    question = python_questions[random]['question']     #stores the path of a random question 
    options = python_questions[random]['options']       #stores the path of a random questions option
    correct_answer = python_questions[random]['answer'] #stores the path of a random questions answer

    print(f"Q. {question}")         #display that random question
    for index, option in enumerate(options):    
        print(f"{index+1}. {option}")   #display that questions options
    
    print("Enter only option not full answer.") 
    user = int(input("Enter your answer :- "))  #take user input as a intiger of usser answer
    answer = options[user-1]        #convert that int input in real answer

    if answer == correct_answer:        #compares the user answer with correct answer and print if answer is correct
        print("correct answer.\n")      
        global correct_score
        correct_score += 1              #add one in correct answer

    else:                               #print wrong answer when answer is wrong
        print("wrong answer.\n")
        global wrong_score
        wrong_score += 1                #add one in wrong score


#same proccess with gk questions
def display_gk_questions():
    random = int(randint(0,49))
    question = gk_questions[random]['question']
    options = gk_questions[random]['options']
    correct_answer = gk_questions[random]['answer']

    print(f"Q. {question}")
    for index, option in enumerate(options):
        print(f"{index+1}. {option}")
    
    print("Enter only option not full answer.")
    user = int(input("Enter your answer :- "))
    answer = options[user-1]

    if answer == correct_answer:
        print("correct answer.\n")
        global correct_score
        correct_score += 1

    else:
        print("wrong answer.\n")
        global wrong_score
        wrong_score += 1


#same proccess with cs questions
def display_cs_questions():
    random = int(randint(0,49))
    question = cs_questions[random]['question']
    options = cs_questions[random]['options']
    correct_answer = cs_questions[random]['answer']

    print(f"Q. {question}")
    for index, option in enumerate(options):
        print(f"{index+1}. {option}")
    
    print("Enter only option not full answer.")
    user = int(input("Enter your answer :- "))
    answer = options[user-1]

    if answer == correct_answer:
        print("correct answer.\n")
        global correct_score
        correct_score += 1

    else:
        print("wrong answer.\n")
        global wrong_score
        wrong_score += 1


#this fuction show the end reselt of the quiz
def show_result():

    print(f"""
congratulations {name}, you completed the quiz.
your correct answers are {correct_score}.
your wrong answers are {wrong_score}.
your percetage is :- {(correct_score/10)*100}%.     
""")


#this is a main fuction that controle the flow and call all the functions

def quiz():
    wellcome()      #greet user

    if choice == 1:         #compare the user choice and call required function
        print("you chose python.")
        for i in range(11):
            display_py_questions() 

    elif choice == 2:
        print("you chose general knowledge.")
        for i in range(11):
            display_gk_questions()

    elif choice == 3:
        print("you chose computer science.")
        for i in range(11):
            display_cs_questions()

    show_result()       #show end results

quiz()
