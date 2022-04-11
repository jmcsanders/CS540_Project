import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


 
 
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="Alice548511",
                               database="Project",
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

 
# USER INPUT BY CITY

mycursor.execute('SELECT mkt_unique_carrier, AVG(dep_delay) FROM flight JOIN (delay,segment) ON (flight.FLIGHT_ID = delay.DELAY_ID AND flight.flight_id = segment.Segment_id) WHERE (MKT_UNIQUE_CARRIER = "UA" OR MKT_UNIQUE_CARRIER = "WN") AND (delay.DEP_DELAY > 0) AND (origin_city LIKE "%Denver%") GROUP BY mkt_unique_carrier')
result = mycursor.fetchall

carrier = []
averages = []
 
for i in mycursor:
    carrier.append(i[0])
    averages.append(i[1])


     
print("mkt_unique_carrier = ", carrier)
print("avearges = ", averages)
 
 # Visulizing Data using Matplotlib
plt.bar(carrier, averages)
plt.ylim(0, 50)
plt.xlabel("Airlines")
plt.ylabel("Average delays in minutes")
plt.title("Airlines Departure Delays for city of 'Denver'")
plt.show()


#USER INPUT BY STATE

mycursor.execute('SELECT mkt_unique_carrier, AVG(dep_delay) FROM flight JOIN (delay,segment) ON (flight.FLIGHT_ID = delay.DELAY_ID AND flight.flight_id = segment.Segment_id) WHERE (MKT_UNIQUE_CARRIER = "UA" OR MKT_UNIQUE_CARRIER = "WN") AND (delay.DEP_DELAY > 0) AND (origin_state_abr LIKE "%FL%") GROUP BY mkt_unique_carrier')
result = mycursor.fetchall


carrier = []
count = []

 
for i in mycursor:
    carrier.append(i[0])
    count.append(i[1])

     
print("mkt_unique_carrier = ", carrier)
print("counts = ", count)

 
 # Visulizing Data using Matplotlib
plt.bar(carrier, count)
plt.ylim(0, 50)
plt.xlabel("Airlines")
plt.ylabel("Count of delays")
plt.title("Airlines Departure Delays for state of 'FL'")
plt.show()

#USER INPUT BY AIRLINES
mycursor.execute('SELECT mkt_unique_carrier, sum(dep_delay)/sum(dep_delay+cancelled+carrier_delay+weather_delay+security_delay+late_aircraft_delay)*100, sum(CANCELLED)/sum(dep_delay+cancelled+carrier_delay+weather_delay+security_delay+late_aircraft_delay)*100, sum(carrier_delay)/sum(dep_delay+cancelled+carrier_delay+weather_delay+security_delay+late_aircraft_delay)*100, sum(weather_delay)/sum(dep_delay+cancelled+carrier_delay+weather_delay+security_delay+late_aircraft_delay)*100, sum(nas_delay)/sum(dep_delay+cancelled+carrier_delay+weather_delay+security_delay+late_aircraft_delay)*100, sum(security_delay)/sum(dep_delay+cancelled+carrier_delay+weather_delay+security_delay+late_aircraft_delay)*100, sum(late_aircraft_delay)/sum(dep_delay+cancelled+carrier_delay+weather_delay+security_delay+late_aircraft_delay)*100 from flight join (DELAY,cause) on (flight.flight_id=cause.cause_id AND flight.flight_id=DELAY.DELAY_id) WHERE (MKT_UNIQUE_CARRIER = "WN" OR MKT_UNIQUE_CARRIER ="UA") GROUP BY mkt_unique_carrier')

# Data to plot
labels = ['Dep_delay', 'Cancelled', 'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aicraft_delay']
percentages = []
for i in mycursor:
    percentages.append(i[1])
    percentages.append(i[2])
    percentages.append(i[3])
    percentages.append(i[4])
    percentages.append(i[5])
    percentages.append(i[6])
    percentages.append(i[7])
print("Percentages =", percentages)

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'blue', 'cyan', 'purple']
explode = (0.1, 0, 0, 0.1, 0, 0, 0.1)  # explode  slice

# Plot
plt.pie(percentages, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.xlabel("Percentage of delays by cause for WN")
plt.show()

#USER INPUT BY AIPPORT 
mycursor.execute('SELECT day_of_week, avg(delay.DEP_DELAY) FROM FLIGHT JOIN (delay,SEGMENT) ON (flight.flight_ID = segment.SEGMENT_ID AND flight.flight_id = delay.delay_id) WHERE segment.ORIGIN like "%STL%" AND delay.DEP_DELAY > 0 AND day_of_week =1 OR day_of_week =2 or day_of_week=3 or day_of_week=4 or day_of_week=5 or day_of_week=6 or day_of_week=7 group by day_of_week')
result = mycursor.fetchall

#Average delay including where there is no delay
#mycursor.execute('SELECT day_of_week, avg(delay.DEP_DELAY) FROM FLIGHT JOIN (delay,SEGMENT) ON (flight.flight_ID = segment.SEGMENT_ID AND flight.flight_id = delay.delay_id) WHERE segment.ORIGIN like "%STL%" AND delay.DEP_DELAY > 0 AND day_of_week > 0 group by day_of_week')

day = []
delay = []

for i in mycursor:
    day.append(i[0])
    delay.append(i[1])

print("day = ", day)
print("delay = ", delay)

plt.bar(day, delay)
plt.ylim(0, 30)
plt.xlabel("days of week\n (1:Sunday, 2:Monday 3:Tuesday, 4:Wednesday, 5:Thrursday, 6:Friday, 7:Saturday)")
plt.ylabel("Average delays(min)")
plt.title("Average Delay at STL when there is a delay")
plt.show()


types_of_delay = ['Carrier_delay',
		'Weather_delay', 'Nas_delay', 'Security_delay', 'Late_aircraft_delay']

data = [7419, 451, 8322, 51, 6956]


# Creating explode data for all the delay causes not incluant dep_delay which is caused by the causes 
# such as carrier,nas,weather,security,late_aircraft 
# Creating color parameters
colors = ( "green", "cyan", "brown",
		"grey", "blue", "beige")

# Wedge properties
wp = { 'linewidth' : 1, 'edgecolor' : "grey" }

# Creating autocpt arguments
def func(pct, allvalues):
	absolute = int(pct / 100.*np.sum(allvalues))
	return "{:.1f}%\n({:d} min)".format(pct, absolute)

# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
								autopct = lambda pct: func(pct, data),
								labels = types_of_delay,
								shadow = True,
								colors = colors,
								startangle = 90,
								wedgeprops = wp,
								textprops = dict(color ="black"))

# Adding legend
ax.legend(wedges, types_of_delay,
		title ="causes",
		loc ="center left",
		bbox_to_anchor =(1, 0, 0.5, 1))

plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Pie chart of Delay causes by total minutes for major airlines\n" + "(AA, AS, B6, DL, F9, G4, HA, NK, UA, WN)\n"+"Year 2021")

# show plot
plt.show()
