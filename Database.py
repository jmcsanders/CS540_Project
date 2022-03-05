from sqlite3 import Row
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

#
# Connect to MySQL Workbench local
#
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='P4he7qv*', database='FlightData')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Connected to database: ", record)


        #
        # Average Delay Time by Airline
        # Hard coded in this case to 'WN' for Southwest Airlines for testing
        #
        # Selects the average from the delay time from entires that are more than 1, indicating a delay
        #
        cursor.execute("SELECT avg(delay.DEP_DELAY) FROM (delay INNER JOIN flight ON delay.DELAY_ID = flight.FLIGHT_ID) WHERE  flight.MKT_UNIQUE_CARRIER = 'WN' AND delay.DEP_DELAY > 0")
        query = (cursor.fetchone()[0])
        print(query)


        #
        # Chance of Delay by Airline
        # Hard coded in this case to 'WN' for Southwest Airlines for testing
        # 
        # Selects the count of entires that are delayed and on time to calculate the chance of a delay for a certain airline
        # Multiplies result by 100 to represent a percentage
        #
        cursor.execute("SELECT count(delay.DEP_DELAY) FROM (delay INNER JOIN flight ON delay.DELAY_ID = flight.FLIGHT_ID) WHERE  flight.MKT_UNIQUE_CARRIER = 'WN' AND delay.DEP_DELAY = 0")
        on_time = (cursor.fetchone()[0])
        cursor.execute("SELECT count(delay.DEP_DELAY) FROM (delay INNER JOIN flight ON delay.DELAY_ID = flight.FLIGHT_ID) WHERE  flight.MKT_UNIQUE_CARRIER = 'WN' AND delay.DEP_DELAY > 0")
        delayed = (cursor.fetchone()[0])

        result = (delayed / (on_time + delayed)) * 100
        print(result)


        #
        # Chance of cancelation by Airline
        # Hard coded in this case to 'WN' for Southwest Airlines for testing
        # 
        # Selects the count of entires that are cancelled and not cancelled to calculate the chance of a cancellation for a certain airline
        # Multiplies result by 100 to represent a percentage
        #
        cursor.execute("SELECT count(delay.CANCELLED) FROM (delay INNER JOIN flight ON delay.DELAY_ID = flight.FLIGHT_ID) WHERE  flight.MKT_UNIQUE_CARRIER = 'WN' AND delay.CANCELLED = 0")
        on_time = (cursor.fetchone()[0])
        cursor.execute("SELECT count(delay.CANCELLED) FROM (delay INNER JOIN flight ON delay.DELAY_ID = flight.FLIGHT_ID) WHERE  flight.MKT_UNIQUE_CARRIER = 'WN' AND delay.CANCELLED = 1")
        delayed = (cursor.fetchone()[0])

        result = (delayed / (on_time + delayed)) * 100
        print(result)        


        #
        # Average Delay Time by Departure Airport
        # Hard coded in this case to 'STL' for testing
        #
        # Selects the average from the delay time from entires that are more than 1, indicating a delay
        #
        cursor.execute("SELECT avg(delay.DEP_DELAY) FROM (delay INNER JOIN segment ON delay.DELAY_ID = segment.SEGMENT_ID) WHERE  segment.ORIGIN = 'STL' AND delay.DEP_DELAY > 0;")
        query = (cursor.fetchone()[0])
        print(query)


        #
        # Chance of Delay by Departure Airport
        # Hard coded in this case to 'STL' for testing
        #
        # Selects the count of entires that are delayed and on time to calculate the chance of a delay for a certain departure airport
        # Multiplies result by 100 to represent a percentage
        #
        cursor.execute("SELECT count(delay.DEP_DELAY) FROM (delay INNER JOIN segment ON delay.DELAY_ID = segment.SEGMENT_ID) WHERE  segment.ORIGIN = 'STL' AND delay.DEP_DELAY = 0;")
        on_time = (cursor.fetchone()[0])
        cursor.execute("SELECT count(delay.DEP_DELAY) FROM (delay INNER JOIN segment ON delay.DELAY_ID = segment.SEGMENT_ID) WHERE  segment.ORIGIN = 'STL' AND delay.DEP_DELAY > 0;")
        delayed = (cursor.fetchone()[0])

        result = (delayed / (on_time + delayed)) * 100
        print(result)


        #
        # Chance of cancelation by Deparure Airport
        # Hard coded in this case to 'STL' for testing
        # 
        # Selects the count of entires that are cancelled and not cancelled to calculate the chance of a cancellation for a certain departure airport
        # Multiplies result by 100 to represent a percentage
        #
        cursor.execute("SELECT count(delay.CANCELLED) FROM (delay INNER JOIN segment ON delay.DELAY_ID = segment.SEGMENT_ID) WHERE  segment.ORIGIN = 'STL' AND delay.CANCELLED = '0'")
        on_time = (cursor.fetchone()[0])
        cursor.execute("SELECT count(delay.CANCELLED) FROM (delay INNER JOIN segment ON delay.DELAY_ID = segment.SEGMENT_ID) WHERE  segment.ORIGIN = 'STL' AND delay.CANCELLED = '1'")
        delayed = (cursor.fetchone()[0])

        result = (delayed / (on_time + delayed)) * 100
        print(result)   




        #
        #
        #
        


except Error as e:
    print("Error while connecting to MySQL", e)


