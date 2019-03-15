import random
import nashpy as nash
import numpy as np

'''
Create list of attributes confidence and attraction level, randomly
'''

def date_attributes(n_list):
    attributes = []
    for i in range(n_list):
        your_confidence = random.randint(0,4)
        attraction_to_other_person = random.randint(0,9)
        attributes.append([your_confidence, attraction_to_other_person])
    return attributes
        
group1 = date_attributes(50)
group2 = date_attributes(50)

print(group1)
print(group2)
