import random
import xlrd

option = ['A','B','C']
"""random_list = []
def random_gen(total_ques):
    r = random.randint(0,total_ques)
    if r not in random_list:
        random_list.append(r)
    else:
        random_gen(total_ques)
    return r"""

def levelup(a):
    if a<=2:
        a+=1
    elif a==3:
        a=3
    return a

def leveldown(a):
    if a>=2:
        a-=1
    elif a==1:
        a=1
    return a

def quiz():
    score=0         #to keep the score
    questionsright=0
    que_dict={} # Keeps in track the questions answered are correct or incorrect

    filename = "questions.xlsx"
    wb = xlrd.open_workbook(filename, encoding_override="utf-8") 
    quizfile = wb.sheet_by_index(0)             #sheet 0 in the excel file

    #to find the total number of questions in the sheet
    tot_que = len(quizfile.col(0))
    print("There are a total of {} questions. ".format(tot_que))
    nq = int(input(" Please enter the total number of questions to be asked: "))
    questionno = 1
    l=2
    a=0
    i=1
    while (i<=nq): # Condition to show only the desired number of questions
        while(a<tot_que) : # Condition to traverse through the available number of questions
            if(a not in que_dict.keys()): # Check if a certain question has already been asked
                question = str(quizfile.cell_value(a,0))+"\n A "+ str(quizfile.cell_value(a,1)) + "\n B " + str(quizfile.cell_value(a,2))+ "\n C "+str(quizfile.cell_value(a,3))
                Corranswers = str(quizfile.cell_value(a,5))
                level= int(quizfile.cell_value(a,6))

                if(level != l): # Determines the correct difficulty level question is asked
                    a+=1
                else:
                    print(Corranswers) #to get ans while testing, comment this before deployment
                    print("Level",level)
                    print("Question #", questionno)
                    print(question)
                    answer = input("Your answer is(A/B/C): ")
                    while (answer.upper() not in option):
                         answer = input(answer + " is not a valid option,please choose A, B or C: ") 
                    if(answer.upper() == Corranswers): # Checks if answer is correct
                        que_dict[a]= 1
                        score = score+1
                        questionsright = questionsright + 1
                        questionno = questionno + 1
                        l=levelup(l)
                        a+=1
                        break
                
                    else: # Checks if answer is incorrect
                        que_dict[a]= 0
                        questionno = questionno + 1
                        l=leveldown(l)
                        a+=1
                        break
        i=i+1               
    totalscore = (score/nq) * 100
    print("You got ", score, "questions right, and a score of ", totalscore, "%.")
    print(que_dict)
quiz()