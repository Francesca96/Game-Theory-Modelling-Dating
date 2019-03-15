
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import statistics

equilibria = equilibria_speed_dates(A,B)

def plot_love_happens(personA, personB, nash_equilibria):
    x = []
    y = []
    colour = []
    for c in range(len(personA)):
        average_attraction_level = sum([personA[c][1], personB[c][1]])
        #print(nash_equilibria[c][0][1][0])
        chance_love_happens_1 = (nash_equilibria[c][0][0][0]) * (nash_equilibria[c][0][1][0])
        x.append(average_attraction_level)
        y.append(chance_love_happens_1)
        colour.append('red')
        if (len(nash_equilibria[c])) >= 2:
            chance_love_happens_2 = (nash_equilibria[c][1][0][0]) * (nash_equilibria[c][1][1][0])
            x.append(average_attraction_level)
            y.append(chance_love_happens_2)
            colour.append('blue')
        if (len(nash_equilibria[c])) >= 3:
            chance_love_happens_3 = (nash_equilibria[c][2][0][0]) * (nash_equilibria[c][2][1][0])
            x.append(average_attraction_level)
            y.append(chance_love_happens_3)
            colour.append('green')
        if (len(nash_equilibria[c])) == 4:
            chance_love_happens_4 = (nash_equilibria[c][3][0][0]) * (nash_equilibria[c][3][1][0])
            x.append(average_attraction_level)
            y.append(chance_love_happens_4)
            colour.append('purple')
    graph = plt.scatter(x, y, s=30, c = colour)
    plt.rcParams["font.family"] = "Skia"
    plt.title("Chance of further date vs. Total attractiveness", fontsize = 15, fontweight = 'bold')
    plt.xlabel("Total attractiveness score of the couple", fontsize = 13)
    plt.ylabel("Chance of a further date", fontsize = 13)
    legend_element1 = [Line2D([0],[0], marker = 'o', color = 'w', label = "First equilibrium", markerfacecolor = 'red', markersize = 6)]
    legend_element2 = [Line2D([0],[0], marker = 'o', color = 'w', label = "Second equilibrium", markerfacecolor = 'blue', markersize = 6)]
    legend_element3 = [Line2D([0],[0], marker = 'o', color = 'w', label = "Third equilibrium", markerfacecolor = 'green', markersize = 6)]
    legend_element4 = [Line2D([0],[0], marker = 'o', color = 'w', label = "Fourth equilibrium", markerfacecolor = 'purple', markersize = 6)]
    plt.legend(handles = legend_element1 + legend_element2 + legend_element3 + legend_element4, loc = 'upper left')
    plt.grid(True)
    #print(x) for debugging purposes
    #print(y) for debugging purposes
    return(graph)
    
    plot_love_happens(group1, group2, equilibria)
