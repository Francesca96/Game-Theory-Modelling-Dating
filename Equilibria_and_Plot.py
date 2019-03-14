def pop_utility_matrix(group):
    utility_matrices = []
    for k in range(len(group)):
        util_matrix = np.array([[0, 0], [0, 0]])
        # Utility for Yes(ask): Yes(ask)
        if group[k][1] <= 4: #Low level of attraction
            util_matrix[0,0] = -((group[k][1])+5)
        elif group[k][0] == 0: #Lowest confidence gives high utility
            util_matrix[0,0] = 5*(group[k][1]) 
        else:
            util_matrix[0,0] = 4*(group[k][1]) 
        #  Utility rejection Yes(ask):No(don't ask)
        util_matrix[0,1] = ((group[k][0])-5)*(group[k][1])
        # Utility No(don't ask):Yes(ask)
        if group[k][1] >= 6:
            #Negative utility as low attraction
            util_matrix[1,0] = -(group[k][1])
        else: 
            #Positive utility as feeling of admiration
            util_matrix[1,0] = 5 - (group[k][0])
        # Utility No(don't ask):No(don't ask)
        if group[k][1] >= 7: #High attraction
            #Feeling of regret for not asking
            util_matrix[1,1] = -((group[k][1])-6)
            #Otherwise 0 utility
        utility_matrices.append(util_matrix)
        if group == group2:
            util_matrix[0,1],util_matrix[1,0] = util_matrix[1,0],util_matrix[0,1]
        #print(util_matrix)
    print(utility_matrices)
    return utility_matrices


A = pop_utility_matrix(group1)
B = pop_utility_matrix(group2)

def equilibria_speed_dates(date1, date2):
    equilibria_results = []
    for r in range(len(date1)):
        speed_date = nash.Game(date1[r], date2[r])
        equilibria_date = speed_date.support_enumeration()
        equilibria_results.append(list(equilibria_date))
    print(equilibria_results)
    return equilibria_results
    
equilibria = equilibria_speed_dates(A,B)

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import statistics
from statistics import mean

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
    print(x)
    print(y)
    return(graph)
    
plot_love_happens(group1, group2, equilibria)
