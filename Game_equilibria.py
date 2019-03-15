'''
Populate utility matrices according to attributes in list from previous function
'''

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

'''
Calculate equilibria for each game using support enumeration
'''

def equilibria_speed_dates(date1, date2):
    equilibria_results = []
    for r in range(len(date1)):
        speed_date = nash.Game(date1[r], date2[r])
        equilibria_date = speed_date.support_enumeration()
        equilibria_results.append(list(equilibria_date))
    print(equilibria_results)
    return equilibria_results
    
equilibria = equilibria_speed_dates(A,B)

