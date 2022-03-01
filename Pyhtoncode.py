#Example of plotting a data chart with python
#Importing libraries
from matplotlib import pyplot as plt
import numpy as np
 
# Creating dataset
flight = ['AA', 'SW', 'DL',
        'UA', 'LH', 'RA']
 #AA= American Airlines, SW= SouthWest Airlines DL=Delta Airlines, UA=United Airlines, LH=Lufthansa, RA=Royal Nepal
data = [23, 17, 35, 29, 12, 41]
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = flight)
 
# show plot
plt.show()