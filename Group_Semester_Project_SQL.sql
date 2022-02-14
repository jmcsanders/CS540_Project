#show databases 
#create database FlightDelays
#use flightdelays
create table all_flight_info(
Quarter int, 
Month int, 
Day_of_Month int, 
Day_of_Week int, 
FL_date date, 
MKT_Unique_Carrier char(2), 
Origin char(3), 
Origin_City_Name varchar(50), 
Origin_State_Abr char(2), 
Dest char(3), 
Dest_City_Name varchar(50), 
Dest_State_Abr char(2), 
Dep_Time int, 
Dep_Delay_New int, 
Cancelled binary(1), 
Carrier_Delay int, 
Weather_Delay int, 
NAS_Delay int, 
Security_Delay int, 
Late_Aircraft_Delay int);