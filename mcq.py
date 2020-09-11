import random

def quiz():
    score=0
    questionsright=0
    filename = "questions.csv"
    quizfile = open(filename, "r")
    nq = int(input(" Please enter the total number of questions to be asked: "))
    quizdata= quizfile.readlines()
    #random.shuffle(quizdata)
    questionno=1
    for i in range(nq):
        x= quizdata[i].strip()
        data= x.split(",")
        question=data[0]+"\n A "+ data[1] + "\n B " + data[2]+ "\n C "+data[3] 
        Corranswers = data[4]
        
        print("Question #",questionno)
        print(question)
        answer=input("Your answer is(A/B/C/D): ")
        if(answer.upper() == Corranswers):
            score=score+1
            questionsright=questionsright+1
            questionno = questionno+1
        else:
            print("Incorrect!")
            questionno = questionno+1
        print()
        
    totalscore= (score/nq)*100
    print("You got ", score, "questions right, and a score of ", totalscore, "%.")
quiz()