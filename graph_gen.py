import matplotlib.pyplot as plt 

def graph(x,y):
    plt.plot(x,y)# plotting the points
    plt.xlabel('Question number')# naming the x axis 
    plt.ylabel('Marks obtained')# naming the y axis 
    plt.title("Graphical Representation of marksheet")# giving a title to the graph
    plt.show()# function to show the plot
    