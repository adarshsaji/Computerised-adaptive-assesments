import random
import xlrd

random_list = []

def random_gen():
    r = random.random()
    if r not in random_list:
        random_list.append(r)
    else:
        random_gen()
    return r

def quiz():
    score=0         #to keep the score
    questionsright=0

    filename = "questions.xlsx"
    wb = xlrd.open_workbook(filename) 
    quizfile = wb.sheet_by_index(0)             #sheet 0 in the excel file

    nq = int(input(" Please enter the total number of questions to be asked: "))
    questionno = 1

    #to find the total number of elements in the sheet
    # total_entries = 0
    # while (quizfile.cell_value(total_entries,0)) != '':
    #     total_entries += 1
    # print(total_entries)

    for i in range(nq):
        #r = random_gen()
        r = nq          #temporary holder for random question number
        question = str(quizfile.cell_value(r,0))+"\n A "+ str(quizfile.cell_value(r,1)) + "\n B " + str(quizfile.cell_value(r,2))+ "\n C "+str(quizfile.cell_value(r,3))
        Corranswers = str(quizfile.cell_value(r,5))
        print(Corranswers)
        print("Question #", questionno)
        print(question)
        answer = input("Your answer is(A/B/C/D): ")
        if(answer.upper() == Corranswers):
            score = score+1
            questionsright = questionsright+1
            questionno = questionno+1
        else:
            print("Incorrect!")
            questionno = questionno+1
        print()
        
    totalscore = (score/nq)*100
    print("You got ", score, "questions right, and a score of ", totalscore, "%.")
quiz()

