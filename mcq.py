import random
import xlrd
import get_detail

random_list = []
option = ['A','B','C']

#random question picker
def random_gen(total_ques):
    r = random.randint(0,total_ques)
    if r not in random_list:
        random_list.append(r)
    else:
        random_gen(total_ques)
    return r
    
def quiz():
    score=0         #to keep the score
    questionsright=0
    get_detail.get_data()
    filename = "questions.xlsx"
    wb = xlrd.open_workbook(filename, encoding_override="utf-8") 
    quizfile = wb.sheet_by_index(0)             #sheet 0 in the excel file

    #to find the total number of questions in the sheet
    tot_que = len(quizfile.col(0))
    print("There are a total of {} questions. ".format(tot_que))
    nq = int(input(" Please enter the total number of questions to be asked: "))
    questionno = 1



    for i in range(nq):
        r = random_gen(tot_que-1)
        #r = i          #temporary holder for random question number
        question = str(quizfile.cell_value(r,0))+"\n A "+ str(quizfile.cell_value(r,1)) + "\n B " + str(quizfile.cell_value(r,2))+ "\n C "+str(quizfile.cell_value(r,3))
        Corranswers = str(quizfile.cell_value(r,5))
        
        print(Corranswers) #to get ans while testing, comment this before deployment

        print("Question #", questionno)
        print(question)
        answer = input("Your answer is(A/B/C): ")
        while (answer.upper() not in option):
             answer = input(answer + " is not a valid option,please choose A, B or C: ") 
        if(answer.upper() == Corranswers):
            score = score+1
            questionsright = questionsright + 1
            questionno = questionno + 1
        else:
            questionno = questionno + 1
            
    totalscore = (score/nq) * 100
    print("You got ", score, "questions right, and a score of ", totalscore, "%.")
    print(random_list)
quiz()

