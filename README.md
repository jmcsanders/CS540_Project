# CS540_Project
CS 540 Semester Project


To run the webapp.py file
1. pip install FLASK
2. pip install flask_sqlalchemy
3. Run code
4. Follow the link at the bottom of the command window (http://127.0.0.1:5001/)
5. 

Running Database.py will connect to the flightdata MySQL database and run queries that will be ran later when the user selects certain options in the GUI. Included queries include -         
        #
        # Average Delay Time by Airline
        # Hard coded in this case to 'WN' for Southwest Airlines for testing
        #
        # Selects the average from the delay time from entires that are more than 1, indicating a delay
        #


        #
        # Chance of Delay by Airline
        # Hard coded in this case to 'WN' for Southwest Airlines for testing
        # 
        # Selects the count of entries that are delayed and on time to calculate the chance of a delay for a certain airline
        # Multiplies result by 100 to represent a percentage
        #


        #
        # Chance of cancelation by Airline
        # Hard coded in this case to 'WN' for Southwest Airlines for testing
        # 
        # Selects the count of entries that are canceled and not canceled to calculate the chance of a cancellation for a certain airline
        # Multiplies result by 100 to represent a percentage
        #


        #
        # Average Delay Time by Departure Airport
        # Hard coded in this case to 'STL' for testing
        #
        # Selects the average from the delay time from entries that are more than 1, indicating a delay
        #


        #
        # Chance of Delay by Departure Airport
        # Hard coded in this case to 'STL' for testing
        #
        # Selects the count of entries that are delayed and on time to calculate the chance of a delay for a certain departure airport
        # Multiplies result by 100 to represent a percentage
        #


        #
        # Chance of cancellation by Deparure Airport
        # Hard coded in this case to 'STL' for testing
        # 
        # Selects the count of entires that are canceled and not canceled to calculate the chance of cancellation for a certain departure airport
        # Multiplies result by 100 to represent a percentage
        #
 
