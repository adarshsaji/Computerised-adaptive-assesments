#import random
import xlrd      #to read the excel file
import time       #to  get the system time

import get_detail
import graph_gen

option = ['A','B','C']          #to validate option input
time_taken = []                 #to store time taken per question

# random_list = []
# def random_gen(total_ques):
#     r = random.randint(0,total_ques)
#     if r not in random_list:
#         random_list.append(r)
#     else:
#         random_gen(total_ques)
#     return r

def levelup(index):
    if index <= 2:
        index += 1
    elif index == 3:
        index = 3
    return index

def leveldown(index):
    if index >= 2:
        index -= 1
    elif index == 1:
        index = 1
    return index

def quiz():
    score = 0         #to keep the score
    questionsright = 0
    que_dict = {}    # Keeps in track the questions answered are correct or incorrect
    que_list = []    # for graphical representation of the result obtained
    lev_list = []    # to calculate the final score
    get_detail.get_data()  #gets name and roll number from the candidate

    filename = "questions.xlsx"
    wb = xlrd.open_workbook(filename, encoding_override="utf-8") 
    quizfile = wb.sheet_by_index(0)             #sheet 0 in the excel file

    #to find the total number of questions in the sheet
    tot_que = len(quizfile.col(0))

    print("There are a total of {} questions. ".format(tot_que))
    #nq = int(input(" Please enter the total number of questions to be asked: "))
    nq = 10
    test_length = int(input('Enter time constarins of test in minutes: '))
    questionno = 1

    Current_level = 2   # Starting difficulty level
    index = 0           # used to store the index of question in excel sheet
    i = 1               # used to iterate nq times 
    
    timeout = float(time.time() + 60*test_length)
    
    while (i <= nq) : # Condition to show only the desired number of questions

        #break the loop if time limit exceeds        
        end_time = float(time.time())
        if end_time > timeout :
            print('Times up!!')
            break

        else :
            while(index < tot_que) : # Condition to traverse through the available number of questions
                if(index not in que_dict.keys()): # Check if a certain question has already been asked
                    question = str(quizfile.cell_value(index,0))+"\n A "+ str(quizfile.cell_value(index,1)) + "\n B " + str(quizfile.cell_value(index,2))+ "\n C "+str(quizfile.cell_value(index,3))
                    Corranswers = str(quizfile.cell_value(index,5))
                    level= int(quizfile.cell_value(index,6))
                    #timeStart = time.time()
                    
                    if(level != Current_level): # Determines the correct difficulty level question is asked
                        index += 1
                    
                    else:
                        t0 = time.time()    
                        print(Corranswers) #to get ans while testing, comment this before deployment
                        print("Level",level)
                        print("Question #", questionno)
                        print(question)
                        answer = input("Your answer is(A/B/C): ")
                        
                        while (answer.upper() not in option):
                            answer = input(answer + " is not a valid option,please choose A, B or C: ") 
                        
                        if(answer.upper() == Corranswers): # Checks if answer is correct
                            que_list.append(index)
                            lev_list.append(Current_level)
                            que_dict[index] = Current_level
                            score += 1
                            #questionsright = questionsright + 1
                            questionno = questionno + 1
                            Current_level = levelup(Current_level)
                            index += 1
                            t1 = time.time() - t0
                            break
                    
                        else: # Checks if answer is incorrect
                            que_list.append(index)
                            lev_list.append(0)
                            que_dict[index] = 0
                            questionno = questionno + 1
                            Current_level = leveldown(Current_level)
                            index += 1
                            t1 = time.time() - t0 
                            break

        time_taken.append(t1)
        #print("Time taken to answer question {} is {:.2f}.".format(questionno-1 , t1))
        i += 1 

    timeEnd = 0
    for ele in range(0, len(time_taken)): 
        timeEnd += time_taken[ele]

    #to calculate total score
    score_keep = 0
    for sco in range(0, len(lev_list)): 
        score_keep += lev_list[sco]

    totalscore = (score_keep/((nq*3)-1)) * 100
    print("You got {} questions right, and a score of {:.2f}%".format(score,totalscore))
    print("Time taken to finish the test :{:.2f}.".format(timeEnd))
    print(que_dict)
    response = que_dict, time_taken
    get_detail.put_data(response)
    graph_gen.graph(lev_list)
    

quiz()