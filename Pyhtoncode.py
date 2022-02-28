# Importing libraries
from matplotlib import pyplot as plt
import numpy as np
 
# Creating dataset
flight = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']
 
data = [23, 17, 35, 29, 12, 41]
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = flight)
 
# show plot
plt.show()