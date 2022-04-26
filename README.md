# CS540_Project
CS 540 Semester Project - Flight Delay Prediction

**Webapp.py**

To run the webapp.py file
1. pip install FLASK
2. pip install flask_sqlalchemy
3. Run code
4. Follow the link at the bottom of the command window (http://127.0.0.1:5001/)


**FlightDelay.sql**

To run FlightDelay.sql
1. Open MySQL server
2. Connect to your server
3. Run code
4. Open new SQL file
5. Write select * from flight;
6. Run line
7. In the result grid, click import records from an external file
8. Select browse
9. Choose "Flight.csv" from your file directory
10. Click next
11. Click existing table (make sure flightdata.flight is selected on drop down menu)
12. Click next
13. Use drop down menus to make every column match
14. Click next
15. Click next
16. Change query line to select * from cause
17. Run line
18. In the result grid, click import records from an external file
19. Select browse
20. Choose "Cause.csv" from your file directory
21. Click next
22. Click existing table (make sure flightdata.cause is selected on drop down menu)
23. Click next
24. Use drop down menus to make every column match
25. Click next
26. Click next
27. Change query line to select * from delay
28. Run line
29. In the result grid, click import records from an external file
30. Select browse
31. Choose "Delays.csv" from your file directory
32. Click next
33. Click existing table (make sure flightdata.delay is selected on drop down menu)
34. Click next
35. Use drop down menus to make every column match
36. Click next
37. Click next
38. Change query line to select * from segment
39. Run line
40. In the result grid, click import records from an external file
41. Select browse
42. Choose "Segment.csv" from your file directory
43. Click next
44. Click existing table (make sure flightdata.segment is selected on drop down menu)
45. Click next
46. Use drop down menus to make every column match
47. Click next
48. Click next

**Database.py**

To run database.py
1. Start MySQL database server
2. Run the python code
3. Output will be numerical values based on calculations of the queried data

Running Database.py will connect to the flightdata MySQL database and run queries that will be ran later when the user selects certain options in the GUI. Included queries include -

        #
        # Average Delay Time by Airline
        # Selects the average from the delay time from entires that are more than 1, indicating a delay
        #
        # Chance of Delay by Airline
        # Selects the count of entries that are delayed and on time to calculate the chance of a delay for a certain airline
        # Multiplies result by 100 to represent a percentage
        #
        # Chance of cancelation by Airline
        # Selects the count of entries that are canceled and not canceled to calculate the chance of a cancellation for a certain airline
        # Multiplies result by 100 to represent a percentage
        #
        # Average Delay Time by Departure Airport
        # Selects the average from the delay time from entries that are more than 1, indicating a delay
        #
        # Chance of Delay by Departure Airport
        # Selects the count of entries that are delayed and on time to calculate the chance of a delay for a certain departure airport
        # Multiplies result by 100 to represent a percentage
        #
        # Chance of cancellation by Deparure Airport
        # Selects the count of entires that are canceled and not canceled to calculate the chance of cancellation for a certain departure airport
        # Multiplies result by 100 to represent a percentage
        #
 
**CS_540_Graphing_Practice.ipynb**

To run CS_540_Graphing_Practice.ipynb

1. Make sure CS_540_Graphing_Practice.ipynb, Flight.csv, Delay.csv, Cause.csv, and Segment.csv are all uploded into Jupyter Notebook
2. Open CS_540_Graphing_Practice.ipynb in Jupyter Notebook
3. Run each cell in Jupyter Notebook by hitting "SHIFT" + "ENTER" on each cell
4. On the Input, type in uppercase letters the Airport Code (e.g., type 'ATL' for Atlanta)
5. Refer to graphs of average delays

*** Note: This file was only used to practice making the graphs / plots for the website using the data set. It still needs to be connected to the database and website. Instead of using Pandas to read the csv files, the data will be brought into the code using MySQL Queries.


**CS540-FlightDelay**
This file contains the updated website interface:

1. To run the current version of the interface for the project website:
2. Open the file and all its dependencies with your text editor , locate index.html 
3. You can run this index.html code within any text editor/to preview it

**Final Flask Website application**
1. Make sure python environment is set up and a python version 3.6 or later is installed.
2. pip install FLASK
3. pip install flask_sqlalchemy
4. Run the code with the following stpes in your text editor's terminal
5. export FLASK_APP=app.py
6. export FLASK_ENV=development
7. flask run --host=0.0.0.0 --port=5004 or whatever available port you prefer in your computer.


