import matplotlib.pyplot as plt 
import xlrd

filename = "stud_detail.xlsx"
wb = xlrd.open_workbook(filename, encoding_override="utf-8") 
detfile = wb.sheet_by_index(0) 
Find_end = len(detfile.col(0)) - 1
name = str(detfile.cell_value(Find_end,0))
roll = str(detfile.cell_value(Find_end,1))
def graph(y):
    x = []
    
    for i in range(len(y)):
        x.append(i)

    plt.plot(x,y)                                           # plotting the points
    plt.xlabel('Question number')                           # naming the x axis 
    plt.ylabel('Marks obtained')                            # naming the y axis 
    plt.title("Result of {} Rollnumber {}".format(name, roll))  # giving a title to the graph
    plt.show()                                              # function to show the plot
    plt.savefig()