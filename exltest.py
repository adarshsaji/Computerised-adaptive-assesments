
import random
import xlrd
def quiz():
    score=0
    questionsright=0
    filename = "questions.xlsx"
    wb = xlrd.open_workbook(filename) 
    quizfile = wb.sheet_by_index(0) 
    nq = int(input(" Please enter the total number of questions to be asked: "))
    #quizdata= quizfile.readlines()
    #random.shuffle(quizdata)
    questionno = 1
    for i in range(nq):
        #x = quizdata[i].strip()
        #data = x.split(",")
        question = str(quizfile.cell_value(i,0))+"\n A "+ str(quizfile.cell_value(i,1)) + "\n B " + str(quizfile.cell_value(i,2))+ "\n C "+str(quizfile.cell_value(i,3))
        Corranswers = str(quizfile.cell_value(i,4))
        
        print("Question #", questionno)
        print(question)
        answer = input("Your answer is(A/B/C/D): ")
        print("hello :"+ Corranswers)
        if(Corranswers == ''):
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