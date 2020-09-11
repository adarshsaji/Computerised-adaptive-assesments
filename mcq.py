import random

def quiz():
    score=0
    questionsright=0
    filename = "Book1.csv"
    quizfile = open(filename, "r")
    nq = int(input(" Please enter the total number of questions to be asked: "))
    quizdata= quizfile.readlines()
    random.shuffle(quizdata)
    questionno=1
    for i in range(nq):
        x= quizdata[i].strip()
        data= x.split(",")
        question=data[0]+data[1]+data[2]+data[3]+data[4]
        Corranswers= data[5]
        
        print("Question #",questionno)
        print(question)
        answer=input("Your answer is(A/B/C/D): ")
        if(answer == Corranswers):
            score=score+1
            questionsright=questionsright+1
            questionno = questionno+1
        else:
            print("Incorrect!")
            questionno = questionno+1
        print()
        
    totalscore= (score/10)*100
    print("You got ", score, "questions right, and a score of ", totalscore, "%.")
quiz()