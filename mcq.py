import random

def quiz():
    score=0
    questionsright=0
    filename = input(" Please enter the name of the quiz file: ")
    quizfile = open(filename, "r")
    #noofquestions = input(" Please enter the total number of questions to be asked: ")
    quizdata= quizfile.readlines()
    random.shuffle(quizdata)
    questionno=1
    for i in range(5):
        x= quizdata[i].strip()
        data= x.split(",")
        question=data[0]
        Corranswers= data[1]
        
        print("Question #",questionno)
        print(question)
        answer=input("Your answer is(A/b/C/D): ")
        if(answer == Corranswer):
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