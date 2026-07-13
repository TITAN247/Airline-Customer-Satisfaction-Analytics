# import pandas as pd
# df=pd.read_csv("airline.csv")
# # print(df.to_string())
# print("displaying thee dataset")
# print(df)
# print("first five data")
# print(df.head())
# print("last five data")
# print(df.tail())
# print("shape of the dataset")
# print(df.shape)
# print("column names")
# print(df.columns)
# print("dataset datatype")
# print(df.dtypes)
# print("information of the dataset")
# print(df.info())
# print("stastical data")
# print(df.describe())
# print("finding missing values")
# print(df.isnull().sum())
# # print("filling missing values by mean ")
# df["Arrival Delay in Minutes"]=df["Arrival Delay in Minutes"].fillna(df["Arrival Delay in Minutes"].mean())
# print("after flling missing values")
# print(df.isnull().sum())
# print("finding duplicate values")
# print(df.duplicated().sum())
# df.drop_duplicates(inplace=True)#changes made in original data
# print(df)
# df.rename(columns={
#     "Customer Type":"Customer_Type",
#     "Type of Travel":"Travel_Type",
#     "Flight Distance":"Flight_Distance",
#     "Seat comfort":"Seat_Comfort",
#     "Food and drink":"Food_Drink",
#     "Gate location":"Gate_Location",
#     "Inflight wifi service":"Wifi_Service",
#     "Inflight entertainment":"Entertainment",
#     "Online support":"Online_Support",
#     "Ease of Online booking":"Online_Booking",
#     "On-board service":"Onboard_Service",
#     "Leg room service":"Legroom_Service",
#     "Baggage handling":"Baggage_Handling",
#     "Checkin service":"Checkin_Service",
#     "Online boarding":"Online_Boarding",
#     "Departure Delay in Minutes":"Departure_Delay",
#     "Arrival Delay in Minutes":"Arrival_Delay"
# },inplace=True)
# print("column updated successfully")
# print(df)
# print("checking data type")
# print(df.dtypes)
# print("changing the datatype")
# df["Departure_Delay"]=pd.to_numeric(df["Departure_Delay"],
# errors="coerce")
# print(df)


# print("Negative Age :",(df["Age"] < 0).sum())

# print("Negative Flight Distance :",(df["Flight_Distance"] < 0).sum())

# print("Negative Arrival Delay :", (df["Arrival_Delay"] < 0).sum())

# print("Negative Departure Delay :",(df["Departure_Delay"] < 0).sum())

# print(df.isnull().sum())
# print(df.shape)


# # print("total number of passenger :",df["id"].count())
# # print(df.columns)

# print("total number of passengers:",df.shape[0])
# print("average pasanger age :",round(df["Age"].mean(),2))
# print("youngest pasanger : ",df["Age"].min())
# print("oldest passenger:",df["Age"].max())
# print("type of customer: ",df["Customer_Type"].value_counts())
# print("type od travel:",df["Travel_Type"].value_counts())

# print("type of travel class:",df["Class"].value_counts())
# print("most preferred class:",df["Class"].value_counts().idxmax())
# print("least preferred class:",df["Class"].value_counts().idxmin())
# print(f"Average flight distance:,{round(df["Flight_Distance"].mean(),2)}km")
# print(f"maximum flight distace:{df["Flight_Distance"].max()}km")
# print(f"Minimum flight distance:{df["Flight_Distance"].min()}km")
# print(f"Average departure delay:{round(df["Departure_Delay"].mean(),2)}minutes")
# print(f"Maximum departure delay:{df["Departure_Delay"].max()}minutes")
# print(f"Minimum departure delay:{df["Departure_Delay"].min()}minutes")
# print(f"Average arrival Delay:{round(df["Arrival_Delay"].mean(),2)}minutes")
# print(f"Maximum arrival delay:{df["Arrival_Delay"].max()}minutes")
# print(f"Minimum arrival delay:{df["Arrival_Delay"].min()}minutes")


# print(df["satisfaction"].value_counts())
# print(round(df["satisfaction"].value_counts(normalize=True)*100,2))


# customer = df.groupby("Customer_Type")["satisfaction"].value_counts()
# print(customer)


# travel = df.groupby("Travel_Type")["satisfaction"].value_counts()
# print(travel)

# travel_class = df.groupby("Class")["satisfaction"].value_counts()
# print(travel_class)


# print("average age :",{round(df["Age"].mean(),2)})
# print("maximum age:",{df["Age"].max()})
# print("minimum age:",{df["Age"].min()})



# distance = df.groupby("satisfaction").agg({"Flight_Distance":["mean","min","max"]})
# print(distance)


# departure = df.groupby("satisfaction").agg({"Departure_Delay":["mean","min","max"]})
# print(departure)



# arrival = df.groupby("satisfaction").agg({ "Arrival_Delay":["mean","min","max"]})
# print(arrival)


# services = [

#     "Seat_Comfort",

#     "Departure/Arrival time convenient",

#     "Food_Drink",

#     "Gate_Location",

#     "Wifi_Service",

#     "Entertainment",

#     "Online_Support",

#     "Online_Booking",

#     "Onboard_Service",

#     "Legroom_Service",

#     "Baggage_Handling",

#     "Checkin_Service",

#     "Cleanliness",

#     "Online_Boarding"

# ]


# average_rating = df[services].mean().round(2)
# print(average_rating)


# ranking = average_rating.sort_values(ascending=False)
# print(ranking)


# print("Service :", ranking.idxmax())

# print("Average Rating :", ranking.max())



# print("Service :", ranking.idxmin())

# print("Average Rating :", ranking.min())



# print(ranking.head())
# print(ranking.tail())


# delay_report = df.groupby("satisfaction").agg({"Departure_Delay":["mean","max","min"],"Arrival_Delay":["mean","max","min"]})
# print(delay_report)



# customer_delay = df.groupby("Customer_Type").agg({ "Departure_Delay":"mean","Arrival_Delay":"mean"}).round(2)
# print(customer_delay)




# travel_delay = df.groupby("Travel_Type").agg({"Departure_Delay":"mean","Arrival_Delay":"mean"}).round(2)

# print(travel_delay)


# class_delay = df.groupby("Class").agg({"Departure_Delay":"mean","Arrival_Delay":"mean"}).round(2)

# print(class_delay)

# late_departure = df.query("Departure_Delay > 60")

# late_arrival = df.query("Arrival_Delay > 60")

# print("Departure Delayed Flights :", late_departure.shape[0])

# print("Arrival Delayed Flights :", late_arrival.shape[0])


# print(df.sort_values( by="Departure_Delay",ascending=False).head(10))



# print(df.sort_values( by="Arrival_Delay",ascending=False).head(10))

# def age_group(age):

#     if age <= 12:
#         return "Child"

#     elif age <= 19:
#         return "Teen"

#     elif age <= 59:
#         return "Adult"

#     else:
#         return "Senior"

# df["Age_Group"] = df["Age"].apply(age_group)

# print(df[["Age","Age_Group"]].head())


# def delay_status(delay):

#     if delay == 0:
#         return "On Time"

#     elif delay <= 30:
#         return "Minor Delay"

#     else:
#         return "Major Delay"

# df["Delay_Status"] = df["Departure_Delay"].apply(delay_status)

# print(df[["Departure_Delay","Delay_Status"]].head())



# print("\nPassengers Age > 60")

# print(df.query("Age > 60").head())

# print("\nBusiness Class Passengers")

# print(df.query("Class == 'Business'").head())

# print("\nSatisfied Customers")

# print(df.query("satisfaction == 'satisfied'").head())

# print("\nFlight Distance > 3000 Km")

# print(df.query("Flight_Distance > 3000").head())


# df["Modified_Departure_Delay"] = df["Departure_Delay"].where(df["Departure_Delay"] <= 60,60)

# print(df[["Departure_Delay","Modified_Departure_Delay"]].head(10))


# df["Modified_Arrival_Delay"] = df["Arrival_Delay"].mask(df["Arrival_Delay"] > 60,60)

# print(df[["Arrival_Delay","Modified_Arrival_Delay"]].head(10))


# age_analysis = df.groupby("Age_Group").agg({ "Flight_Distance":["mean","max","min"], "Departure_Delay":["mean","max"],"Arrival_Delay":["mean","max"]}).round(2)

# print(age_analysis)


# print(df.groupby("Age_Group")["satisfaction"].value_counts())

# print(df["Delay_Status"].value_counts())



# airline_info = pd.DataFrame({

#     "Class":["Business","Eco","Eco Plus"],

#     "Ticket_Price":[15000,7000,10000],

#     "Lounge_Access":["Yes","No","Limited"]

# })

# print(airline_info)



# merged_df = pd.merge(df,airline_info,on="Class",how="left")

# print(merged_df.head())

# airport = pd.DataFrame({

#     "Airport":["Delhi","Mumbai","Bangalore"],

#     "Code":["DEL","BOM","BLR"]
# })

# airport.index = [0,1,2]

# join_df = airline_info.join(airport)

# print(join_df)


# business = df[df["Class"]=="Business"].head(5)

# eco = df[df["Class"]=="Eco"].head(5)

# combined = pd.concat( [business,eco], ignore_index=True)

# print(combined)


# sample = pd.DataFrame({

#     "Service":["Seat Comfort","WiFi","Food"],

#     "Rating":[4,3,5]

# })
# print(sample)
# print(sample.stack())



# services = [

#     "Seat_Comfort",

#     "Departure/Arrival time convenient",

#     "Food_Drink",

#     "Gate_Location",

#     "Wifi_Service",

#     "Entertainment",

#     "Online_Support",

#     "Online_Booking",

#     "Onboard_Service",

#     "Legroom_Service",

#     "Baggage_Handling",

#     "Checkin_Service",

#     "Cleanliness",

#     "Online_Boarding"

# ]
# service_rating = df[services].mean().round(2)
# print(f"Total Passengers                 : {df.shape[0]}")

# print(f"Average Passenger Age            : {round(df['Age'].mean(),2)} Years")

# print(f"Youngest Passenger               : {df['Age'].min()} Years")

# print(f"Oldest Passenger                 : {df['Age'].max()} Years")

# print(f"Average Flight Distance          : {round(df['Flight_Distance'].mean(),2)} Km")

# print()



# ==================================================================================================
#                     AIRLINE CUSTOMER SATISFACTION ANALYSIS USING PANDAS
# --------------------------------------------------------------------------------------------------
# Author      : Shivansh Chaurasiya
# Language    : Python
# Library     : Pandas
#
# Description:
# This project performs a complete analysis of Airline Customer Satisfaction data using Pandas.
# The project covers:
#
#   ✓ Data Loading
#   ✓ Data Cleaning
#   ✓ Exploratory Data Analysis
#   ✓ Customer Satisfaction Analysis
#   ✓ Airline Service Analysis
#   ✓ Delay Analysis
#   ✓ Advanced Pandas Functions
#   ✓ Merge, Join, Concat & Stack
#   ✓ Final Business Report
#
# Dataset : airline.csv
#
# ==================================================================================================



# ==================================================================================================
#                                        MODULE 1
#                             IMPORT LIBRARIES & LOAD DATASET
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Import Required Library
# --------------------------------------------------------------------------------------------------

import pandas as pd



# --------------------------------------------------------------------------------------------------
# Load Dataset
# --------------------------------------------------------------------------------------------------

print("=" * 100)
print("                    AIRLINE CUSTOMER SATISFACTION ANALYSIS")
print("=" * 100)

try:

    # Read the CSV file
    df = pd.read_csv("airline.csv")

    print("\nDataset Loaded Successfully.\n")

except FileNotFoundError:

    print("\nError : airline.csv file was not found.")
    print("Make sure the dataset is present in the current folder.")
    exit()

except pd.errors.EmptyDataError:

    print("\nError : Dataset is empty.")
    exit()

except Exception as e:

    print("\nUnexpected Error :", e)
    exit()



# --------------------------------------------------------------------------------------------------
# Display Complete Dataset
# --------------------------------------------------------------------------------------------------

print("=" * 100)
print("DISPLAYING COMPLETE DATASET")
print("=" * 100)

print(df)



# --------------------------------------------------------------------------------------------------
# Display First Five Records
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("FIRST FIVE RECORDS")
print("=" * 100)

print(df.head())



# --------------------------------------------------------------------------------------------------
# Display Last Five Records
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("LAST FIVE RECORDS")
print("=" * 100)

print(df.tail())



# --------------------------------------------------------------------------------------------------
# Display Dataset Shape
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("DATASET SHAPE")
print("=" * 100)

print(f"Total Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")



# --------------------------------------------------------------------------------------------------
# Display Column Names
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("COLUMN NAMES")
print("=" * 100)

print(df.columns)



# --------------------------------------------------------------------------------------------------
# Display Data Types
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("DATA TYPES")
print("=" * 100)

print(df.dtypes)



# --------------------------------------------------------------------------------------------------
# Dataset Information
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("DATASET INFORMATION")
print("=" * 100)

df.info()



# --------------------------------------------------------------------------------------------------
# Statistical Summary
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("STATISTICAL SUMMARY")
print("=" * 100)

print(df.describe())



# --------------------------------------------------------------------------------------------------
# Display Total Memory Usage
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("MEMORY USAGE")
print("=" * 100)

memory = df.memory_usage(deep=True).sum() / 1024**2

print(f"Total Memory Used : {memory:.2f} MB")



# --------------------------------------------------------------------------------------------------
# Module Completion Message
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("MODULE 1 COMPLETED SUCCESSFULLY")
print("=" * 100)


# ==================================================================================================
#                                        MODULE 2
#                          DATA CLEANING & DATA PREPROCESSING
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Missing Value Analysis
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("MISSING VALUE ANALYSIS")
print("=" * 100)

print(df.isnull().sum())


# --------------------------------------------------------------------------------------------------
# Fill Missing Values
# --------------------------------------------------------------------------------------------------
# Fill missing values in 'Arrival Delay in Minutes' using the mean value

df["Arrival Delay in Minutes"] = df["Arrival Delay in Minutes"].fillna(
    df["Arrival Delay in Minutes"].mean()
)

print("\nMissing Values After Filling")

print(df.isnull().sum())


# --------------------------------------------------------------------------------------------------
# Duplicate Records
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("DUPLICATE RECORD ANALYSIS")
print("=" * 100)

duplicate_records = df.duplicated().sum()

print(f"Total Duplicate Records : {duplicate_records}")


# --------------------------------------------------------------------------------------------------
# Remove Duplicate Records
# --------------------------------------------------------------------------------------------------

df.drop_duplicates(inplace=True)

print("\nDuplicate Records Removed Successfully.")

print(f"Current Dataset Shape : {df.shape}")


# --------------------------------------------------------------------------------------------------
# Rename Column Names
# --------------------------------------------------------------------------------------------------
# Rename columns for easier access

df.rename(columns={

    "Customer Type":"Customer_Type",

    "Type of Travel":"Travel_Type",

    "Flight Distance":"Flight_Distance",

    "Seat comfort":"Seat_Comfort",

    "Food and drink":"Food_Drink",

    "Gate location":"Gate_Location",

    "Inflight wifi service":"Wifi_Service",

    "Inflight entertainment":"Entertainment",

    "Online support":"Online_Support",

    "Ease of Online booking":"Online_Booking",

    "On-board service":"Onboard_Service",

    "Leg room service":"Legroom_Service",

    "Baggage handling":"Baggage_Handling",

    "Checkin service":"Checkin_Service",

    "Online boarding":"Online_Boarding",

    "Departure Delay in Minutes":"Departure_Delay",

    "Arrival Delay in Minutes":"Arrival_Delay"

}, inplace=True)


print("\nColumn Names Updated Successfully.")


# --------------------------------------------------------------------------------------------------
# Display Updated Column Names
# --------------------------------------------------------------------------------------------------

print("\nUpdated Columns\n")

print(df.columns)


# --------------------------------------------------------------------------------------------------
# Data Type Conversion
# --------------------------------------------------------------------------------------------------
# Convert delay columns into numeric format

df["Departure_Delay"] = pd.to_numeric(

    df["Departure_Delay"],

    errors="coerce"

)

df["Arrival_Delay"] = pd.to_numeric(

    df["Arrival_Delay"],

    errors="coerce"

)

print("\nData Types After Conversion")

print(df.dtypes)


# --------------------------------------------------------------------------------------------------
# Data Validation
# --------------------------------------------------------------------------------------------------
# Check for invalid negative values

print("\n" + "=" * 100)
print("DATA VALIDATION")
print("=" * 100)

print("Negative Age Values               :", (df["Age"] < 0).sum())

print("Negative Flight Distance Values   :", (df["Flight_Distance"] < 0).sum())

print("Negative Departure Delay Values   :", (df["Departure_Delay"] < 0).sum())

print("Negative Arrival Delay Values     :", (df["Arrival_Delay"] < 0).sum())


# --------------------------------------------------------------------------------------------------
# Final Missing Value Check
# --------------------------------------------------------------------------------------------------

print("\nFinal Missing Value Report")

print(df.isnull().sum())


# --------------------------------------------------------------------------------------------------
# Display Cleaned Dataset Information
# --------------------------------------------------------------------------------------------------

print("\nDataset Shape After Cleaning")

print(df.shape)


print("\nDataset Information After Cleaning")

df.info()


# --------------------------------------------------------------------------------------------------
# Save Cleaned Dataset
# --------------------------------------------------------------------------------------------------

df.to_csv(

    "cleaned_airline_data.csv",

    index=False

)

print("\nCleaned Dataset Saved Successfully.")

print("File Name : cleaned_airline_data.csv")


# --------------------------------------------------------------------------------------------------
# Data Cleaning Summary Report
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("DATA CLEANING SUMMARY REPORT")
print("=" * 100)

print(f"Total Rows After Cleaning          : {df.shape[0]}")

print(f"Total Columns                      : {df.shape[1]}")

print(f"Duplicate Records Removed          : {duplicate_records}")

print("Missing Values                     : Handled")

print("Column Names                       : Standardized")

print("Data Types                         : Converted")

print("Dataset Status                     : Ready For Analysis")


# --------------------------------------------------------------------------------------------------
# Module Completion Message
# --------------------------------------------------------------------------------------------------

print("\n" + "=" * 100)
print("MODULE 2 COMPLETED SUCCESSFULLY")
print("=" * 100)

# ==================================================================================================
#                                        MODULE 3
#                         PASSENGER & TRAVEL OVERVIEW ANALYSIS
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Project Objective
# --------------------------------------------------------------------------------------------------
# This module provides an overview of passenger demographics,
# customer types, travel patterns, flight distances,
# and delay statistics.
# --------------------------------------------------------------------------------------------------


print("\n" + "=" * 100)
print("PASSENGER & TRAVEL OVERVIEW ANALYSIS")
print("=" * 100)


# ==================================================================================================
# PASSENGER INFORMATION
# ==================================================================================================

print("\n" + "-" * 100)
print("PASSENGER INFORMATION")
print("-" * 100)

print(f"Total Number of Passengers        : {df.shape[0]}")

print(f"Average Passenger Age             : {round(df['Age'].mean(),2)} Years")

print(f"Youngest Passenger                : {df['Age'].min()} Years")

print(f"Oldest Passenger                  : {df['Age'].max()} Years")


# ==================================================================================================
# CUSTOMER TYPE ANALYSIS
# ==================================================================================================

print("\n" + "-" * 100)
print("CUSTOMER TYPE DISTRIBUTION")
print("-" * 100)

customer_type = df["Customer_Type"].value_counts()

print(customer_type)

print("\nMost Common Customer Type :", customer_type.idxmax())

print("Least Common Customer Type :", customer_type.idxmin())


# ==================================================================================================
# TRAVEL TYPE ANALYSIS
# ==================================================================================================

print("\n" + "-" * 100)
print("TRAVEL TYPE DISTRIBUTION")
print("-" * 100)

travel_type = df["Travel_Type"].value_counts()

print(travel_type)

print("\nMost Preferred Travel Type :", travel_type.idxmax())

print("Least Preferred Travel Type :", travel_type.idxmin())


# ==================================================================================================
# TRAVEL CLASS ANALYSIS
# ==================================================================================================

print("\n" + "-" * 100)
print("TRAVEL CLASS DISTRIBUTION")
print("-" * 100)

travel_class = df["Class"].value_counts()

print(travel_class)

print("\nMost Preferred Class :", travel_class.idxmax())

print("Least Preferred Class :", travel_class.idxmin())


# ==================================================================================================
# FLIGHT DISTANCE ANALYSIS
# ==================================================================================================

print("\n" + "-" * 100)
print("FLIGHT DISTANCE ANALYSIS")
print("-" * 100)

print(f"Average Flight Distance           : {round(df['Flight_Distance'].mean(),2)} Km")

print(f"Maximum Flight Distance           : {df['Flight_Distance'].max()} Km")

print(f"Minimum Flight Distance           : {df['Flight_Distance'].min()} Km")


# ==================================================================================================
# DEPARTURE DELAY ANALYSIS
# ==================================================================================================

print("\n" + "-" * 100)
print("DEPARTURE DELAY ANALYSIS")
print("-" * 100)

print(f"Average Departure Delay           : {round(df['Departure_Delay'].mean(),2)} Minutes")

print(f"Maximum Departure Delay           : {df['Departure_Delay'].max()} Minutes")

print(f"Minimum Departure Delay           : {df['Departure_Delay'].min()} Minutes")


# ==================================================================================================
# ARRIVAL DELAY ANALYSIS
# ==================================================================================================

print("\n" + "-" * 100)
print("ARRIVAL DELAY ANALYSIS")
print("-" * 100)

print(f"Average Arrival Delay             : {round(df['Arrival_Delay'].mean(),2)} Minutes")

print(f"Maximum Arrival Delay             : {df['Arrival_Delay'].max()} Minutes")

print(f"Minimum Arrival Delay             : {df['Arrival_Delay'].min()} Minutes")


# ==================================================================================================
# OVERALL PASSENGER SUMMARY REPORT
# ==================================================================================================

print("\n" + "=" * 100)
print("PASSENGER OVERVIEW SUMMARY REPORT")
print("=" * 100)

print(f"Total Passengers                 : {df.shape[0]}")

print(f"Average Age                      : {round(df['Age'].mean(),2)} Years")

print(f"Youngest Passenger               : {df['Age'].min()} Years")

print(f"Oldest Passenger                 : {df['Age'].max()} Years")

print(f"Most Preferred Customer Type     : {customer_type.idxmax()}")

print(f"Most Preferred Travel Type       : {travel_type.idxmax()}")

print(f"Most Preferred Travel Class      : {travel_class.idxmax()}")

print(f"Average Flight Distance          : {round(df['Flight_Distance'].mean(),2)} Km")

print(f"Average Departure Delay          : {round(df['Departure_Delay'].mean(),2)} Minutes")

print(f"Average Arrival Delay            : {round(df['Arrival_Delay'].mean(),2)} Minutes")


# ==================================================================================================
# MODULE COMPLETION
# ==================================================================================================

print("\n" + "=" * 100)
print("MODULE 3 COMPLETED SUCCESSFULLY")
print("=" * 100)

# ==================================================================================================
#                                        MODULE 4
#                          CUSTOMER SATISFACTION ANALYSIS
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Project Objective
# --------------------------------------------------------------------------------------------------
# This module analyzes customer satisfaction based on customer type,
# travel type, travel class, flight distance and delays.
# --------------------------------------------------------------------------------------------------


print("\n" + "=" * 100)
print("CUSTOMER SATISFACTION ANALYSIS")
print("=" * 100)


# ==================================================================================================
# OVERALL SATISFACTION
# ==================================================================================================

print("\n" + "-" * 100)
print("OVERALL CUSTOMER SATISFACTION")
print("-" * 100)

satisfaction = df["satisfaction"].value_counts()

print(satisfaction)


print("\nCustomer Satisfaction Percentage")

print(round(df["satisfaction"].value_counts(normalize=True) * 100, 2))


# ==================================================================================================
# CUSTOMER TYPE VS SATISFACTION
# ==================================================================================================

print("\n" + "-" * 100)
print("CUSTOMER TYPE VS SATISFACTION")
print("-" * 100)

customer_satisfaction = (

    df.groupby("Customer_Type")["satisfaction"]

      .value_counts()

)

print(customer_satisfaction)


# ==================================================================================================
# TRAVEL TYPE VS SATISFACTION
# ==================================================================================================

print("\n" + "-" * 100)
print("TRAVEL TYPE VS SATISFACTION")
print("-" * 100)

travel_satisfaction = (

    df.groupby("Travel_Type")["satisfaction"]

      .value_counts()

)

print(travel_satisfaction)


# ==================================================================================================
# TRAVEL CLASS VS SATISFACTION
# ==================================================================================================

print("\n" + "-" * 100)
print("TRAVEL CLASS VS SATISFACTION")
print("-" * 100)

class_satisfaction = (

    df.groupby("Class")["satisfaction"]

      .value_counts()

)

print(class_satisfaction)


# ==================================================================================================
# AGE ANALYSIS
# ==================================================================================================

print("\n" + "-" * 100)
print("AGE ANALYSIS")
print("-" * 100)

print(f"Average Passenger Age : {round(df['Age'].mean(),2)} Years")

print(f"Youngest Passenger    : {df['Age'].min()} Years")

print(f"Oldest Passenger      : {df['Age'].max()} Years")


# ==================================================================================================
# FLIGHT DISTANCE VS SATISFACTION
# ==================================================================================================

print("\n" + "-" * 100)
print("FLIGHT DISTANCE ANALYSIS")
print("-" * 100)

flight_distance = (

    df.groupby("satisfaction").agg({

        "Flight_Distance":["mean","min","max"]

    }).round(2)

)

print(flight_distance)


# ==================================================================================================
# DEPARTURE DELAY VS SATISFACTION
# ==================================================================================================

print("\n" + "-" * 100)
print("DEPARTURE DELAY ANALYSIS")
print("-" * 100)

departure_delay = (

    df.groupby("satisfaction").agg({

        "Departure_Delay":["mean","min","max"]

    }).round(2)

)

print(departure_delay)


# ==================================================================================================
# ARRIVAL DELAY VS SATISFACTION
# ==================================================================================================

print("\n" + "-" * 100)
print("ARRIVAL DELAY ANALYSIS")
print("-" * 100)

arrival_delay = (

    df.groupby("satisfaction").agg({

        "Arrival_Delay":["mean","min","max"]

    }).round(2)

)

print(arrival_delay)


# ==================================================================================================
# SATISFACTION SUMMARY REPORT
# ==================================================================================================

print("\n" + "=" * 100)
print("CUSTOMER SATISFACTION SUMMARY REPORT")
print("=" * 100)

print(f"Total Passengers                  : {df.shape[0]}")

# Safe way to get satisfaction counts
satisfaction = df["satisfaction"].value_counts()

print(f"Satisfied Customers               : {satisfaction.get('satisfied', 0)}")
print(f"Neutral/Dissatisfied Customers    : {satisfaction.get('neutral or dissatisfied', 0)}")

print(f"Average Flight Distance           : {round(df['Flight_Distance'].mean(),2)} Km")

print(f"Average Departure Delay           : {round(df['Departure_Delay'].mean(),2)} Minutes")

print(f"Average Arrival Delay             : {round(df['Arrival_Delay'].mean(),2)} Minutes")

print(f"Most Common Customer Type         : {df['Customer_Type'].value_counts().idxmax()}")

print(f"Most Common Travel Type           : {df['Travel_Type'].value_counts().idxmax()}")

print(f"Most Preferred Travel Class       : {df['Class'].value_counts().idxmax()}")


# ==================================================================================================
# KEY BUSINESS INSIGHTS
# ==================================================================================================

print("\n" + "=" * 100)
print("KEY BUSINESS INSIGHTS")
print("=" * 100)

print("""
1. Overall customer satisfaction has been successfully analyzed.

2. Satisfaction has been compared across Customer Type.

3. Satisfaction has been compared across Travel Type.

4. Satisfaction has been compared across Travel Class.

5. Flight Distance statistics have been analyzed.

6. Departure Delay and Arrival Delay have been analyzed.

7. These insights can help airline management improve customer experience.
""")


# ==================================================================================================
# MODULE COMPLETION
# ==================================================================================================

print("=" * 100)
print("MODULE 4 COMPLETED SUCCESSFULLY")
print("=" * 100)

# ==================================================================================================
#                                        MODULE 5
#                            AIRLINE SERVICE QUALITY ANALYSIS
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Project Objective
# --------------------------------------------------------------------------------------------------
# This module analyzes the ratings of different airline services.
# It identifies the highest-rated and lowest-rated services and
# generates a complete service quality report.
# --------------------------------------------------------------------------------------------------


print("\n" + "=" * 100)
print("AIRLINE SERVICE QUALITY ANALYSIS")
print("=" * 100)


# ==================================================================================================
# LIST OF SERVICE COLUMNS
# ==================================================================================================

services = [

    "Seat_Comfort",

    "Departure/Arrival time convenient",

    "Food_Drink",

    "Gate_Location",

    "Wifi_Service",

    "Entertainment",

    "Online_Support",

    "Online_Booking",

    "Onboard_Service",

    "Legroom_Service",

    "Baggage_Handling",

    "Checkin_Service",

    "Cleanliness",

    "Online_Boarding"

]


# ==================================================================================================
# AVERAGE RATING OF EACH SERVICE
# ==================================================================================================

print("\n" + "-" * 100)
print("AVERAGE RATING OF EACH SERVICE")
print("-" * 100)

average_rating = df[services].mean().round(2)

print(average_rating)


# ==================================================================================================
# SERVICE RANKING
# ==================================================================================================

print("\n" + "-" * 100)
print("SERVICE RANKING (HIGHEST TO LOWEST)")
print("-" * 100)

ranking = average_rating.sort_values(ascending=False)

print(ranking)


# ==================================================================================================
# TOP 5 SERVICES
# ==================================================================================================

print("\n" + "-" * 100)
print("TOP 5 BEST SERVICES")
print("-" * 100)

print(ranking.head(5))


# ==================================================================================================
# BOTTOM 5 SERVICES
# ==================================================================================================

print("\n" + "-" * 100)
print("BOTTOM 5 SERVICES NEEDING IMPROVEMENT")
print("-" * 100)

print(ranking.tail(5))


# ==================================================================================================
# BEST SERVICE
# ==================================================================================================

print("\n" + "-" * 100)
print("BEST RATED SERVICE")
print("-" * 100)

print(f"Service Name     : {ranking.idxmax()}")

print(f"Average Rating   : {ranking.max()}")


# ==================================================================================================
# LOWEST RATED SERVICE
# ==================================================================================================

print("\n" + "-" * 100)
print("LOWEST RATED SERVICE")
print("-" * 100)

print(f"Service Name     : {ranking.idxmin()}")

print(f"Average Rating   : {ranking.min()}")


# ==================================================================================================
# OVERALL SERVICE QUALITY SCORE
# ==================================================================================================

print("\n" + "-" * 100)
print("OVERALL SERVICE QUALITY")
print("-" * 100)

overall_score = round(average_rating.mean(),2)

print(f"Overall Service Rating : {overall_score}/5")


# ==================================================================================================
# SERVICE QUALITY SUMMARY
# ==================================================================================================

print("\n" + "=" * 100)
print("SERVICE QUALITY SUMMARY REPORT")
print("=" * 100)

print(f"Total Services Analyzed      : {len(services)}")

print(f"Best Rated Service           : {ranking.idxmax()}")

print(f"Highest Rating               : {ranking.max()}")

print(f"Worst Rated Service          : {ranking.idxmin()}")

print(f"Lowest Rating                : {ranking.min()}")

print(f"Overall Average Rating       : {overall_score}")


# ==================================================================================================
# BUSINESS INSIGHTS
# ==================================================================================================

print("\n" + "=" * 100)
print("BUSINESS INSIGHTS")
print("=" * 100)

print("""

1. The airline's strongest service has been identified.

2. The weakest service requiring immediate improvement has been identified.

3. Average ratings have been calculated for every service.

4. All services have been ranked from highest to lowest.

5. These insights help management prioritize service improvements.

""")


# ==================================================================================================
# MODULE COMPLETION
# ==================================================================================================

print("=" * 100)
print("MODULE 5 COMPLETED SUCCESSFULLY")
print("=" * 100)

# ==================================================================================================
#                                        MODULE 6
#                        DELAY ANALYSIS & OPERATIONAL PERFORMANCE
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Project Objective
# --------------------------------------------------------------------------------------------------
# This module analyzes departure and arrival delays and studies
# their relationship with customer satisfaction, customer type,
# travel type, and travel class.
# --------------------------------------------------------------------------------------------------


print("\n" + "=" * 100)
print("DELAY ANALYSIS & OPERATIONAL PERFORMANCE")
print("=" * 100)


# ==================================================================================================
# OVERALL DELAY STATISTICS
# ==================================================================================================

print("\n" + "-" * 100)
print("OVERALL DELAY STATISTICS")
print("-" * 100)

print(f"Average Departure Delay : {round(df['Departure_Delay'].mean(),2)} Minutes")

print(f"Maximum Departure Delay : {df['Departure_Delay'].max()} Minutes")

print(f"Minimum Departure Delay : {df['Departure_Delay'].min()} Minutes")

print()

print(f"Average Arrival Delay   : {round(df['Arrival_Delay'].mean(),2)} Minutes")

print(f"Maximum Arrival Delay   : {df['Arrival_Delay'].max()} Minutes")

print(f"Minimum Arrival Delay   : {df['Arrival_Delay'].min()} Minutes")


# ==================================================================================================
# SATISFACTION VS DELAY
# ==================================================================================================

print("\n" + "-" * 100)
print("CUSTOMER SATISFACTION VS DELAY")
print("-" * 100)

delay_report = df.groupby("satisfaction").agg({

    "Departure_Delay":["mean","max","min"],

    "Arrival_Delay":["mean","max","min"]

}).round(2)

print(delay_report)


# ==================================================================================================
# CUSTOMER TYPE VS DELAY
# ==================================================================================================

print("\n" + "-" * 100)
print("CUSTOMER TYPE VS DELAY")
print("-" * 100)

customer_delay = df.groupby("Customer_Type").agg({

    "Departure_Delay":"mean",

    "Arrival_Delay":"mean"

}).round(2)

print(customer_delay)


# ==================================================================================================
# TRAVEL TYPE VS DELAY
# ==================================================================================================

print("\n" + "-" * 100)
print("TRAVEL TYPE VS DELAY")
print("-" * 100)

travel_delay = df.groupby("Travel_Type").agg({

    "Departure_Delay":"mean",

    "Arrival_Delay":"mean"

}).round(2)

print(travel_delay)


# ==================================================================================================
# CLASS VS DELAY
# ==================================================================================================

print("\n" + "-" * 100)
print("TRAVEL CLASS VS DELAY")
print("-" * 100)

class_delay = df.groupby("Class").agg({

    "Departure_Delay":"mean",

    "Arrival_Delay":"mean"

}).round(2)

print(class_delay)


# ==================================================================================================
# FLIGHTS DELAYED MORE THAN 60 MINUTES
# ==================================================================================================

print("\n" + "-" * 100)
print("FLIGHTS DELAYED MORE THAN 60 MINUTES")
print("-" * 100)

late_departure = df.query("Departure_Delay > 60")

late_arrival = df.query("Arrival_Delay > 60")

print(f"Departure Delayed Flights (>60 min) : {late_departure.shape[0]}")

print(f"Arrival Delayed Flights (>60 min)   : {late_arrival.shape[0]}")


# ==================================================================================================
# TOP 10 DEPARTURE DELAYS
# ==================================================================================================

print("\n" + "-" * 100)
print("TOP 10 HIGHEST DEPARTURE DELAYS")
print("-" * 100)

top_departure = df.sort_values(

    by="Departure_Delay",

    ascending=False

).head(10)

print(top_departure[[
    "Customer_Type",
    "Travel_Type",
    "Class",
    "Departure_Delay"
]])


# ==================================================================================================
# TOP 10 ARRIVAL DELAYS
# ==================================================================================================

print("\n" + "-" * 100)
print("TOP 10 HIGHEST ARRIVAL DELAYS")
print("-" * 100)

top_arrival = df.sort_values(

    by="Arrival_Delay",

    ascending=False

).head(10)

print(top_arrival[[
    "Customer_Type",
    "Travel_Type",
    "Class",
    "Arrival_Delay"
]])


# ==================================================================================================
# DELAY SUMMARY REPORT
# ==================================================================================================

print("\n" + "=" * 100)
print("DELAY ANALYSIS SUMMARY REPORT")
print("=" * 100)

print(f"Average Departure Delay          : {round(df['Departure_Delay'].mean(),2)} Minutes")

print(f"Average Arrival Delay            : {round(df['Arrival_Delay'].mean(),2)} Minutes")

print(f"Maximum Departure Delay          : {df['Departure_Delay'].max()} Minutes")

print(f"Maximum Arrival Delay            : {df['Arrival_Delay'].max()} Minutes")

print(f"Flights Delayed (>60 Minutes)    : {late_departure.shape[0]}")

print(f"Most Delayed Travel Class        : {class_delay['Departure_Delay'].idxmax()}")

print(f"Least Delayed Travel Class       : {class_delay['Departure_Delay'].idxmin()}")


# ==================================================================================================
# BUSINESS INSIGHTS
# ==================================================================================================

print("\n" + "=" * 100)
print("BUSINESS INSIGHTS")
print("=" * 100)

print("""

1. Average departure and arrival delays have been calculated.

2. Delay statistics have been compared across customer satisfaction.

3. Delay statistics have been compared across customer type.

4. Delay statistics have been compared across travel type.

5. Delay statistics have been compared across travel class.

6. Flights delayed by more than 60 minutes have been identified.

7. The top 10 most delayed flights have been listed.

""")


# ==================================================================================================
# MODULE COMPLETION
# ==================================================================================================

print("=" * 100)
print("MODULE 6 COMPLETED SUCCESSFULLY")
print("=" * 100)
# ==================================================================================================
#                                        MODULE 7
#                         ADVANCED PANDAS OPERATIONS
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Project Objective
# --------------------------------------------------------------------------------------------------
# This module demonstrates advanced Pandas functions such as
# apply(), query(), where(), mask(), groupby(), and agg().
# It creates new features and performs advanced data analysis.
# --------------------------------------------------------------------------------------------------


print("\n" + "=" * 100)
print("ADVANCED PANDAS OPERATIONS")
print("=" * 100)


# ==================================================================================================
# CREATE AGE GROUP USING APPLY()
# ==================================================================================================

print("\n" + "-" * 100)
print("CREATING AGE GROUP")
print("-" * 100)


def age_group(age):

    if age <= 12:
        return "Child"

    elif age <= 19:
        return "Teen"

    elif age <= 59:
        return "Adult"

    else:
        return "Senior"


df["Age_Group"] = df["Age"].apply(age_group)

print(df[["Age", "Age_Group"]].head(10))


# ==================================================================================================
# CREATE DELAY STATUS USING APPLY()
# ==================================================================================================

print("\n" + "-" * 100)
print("CREATING DELAY STATUS")
print("-" * 100)


def delay_status(delay):

    if delay == 0:
        return "On Time"

    elif delay <= 30:
        return "Minor Delay"

    else:
        return "Major Delay"


df["Delay_Status"] = df["Departure_Delay"].apply(delay_status)

print(df[["Departure_Delay", "Delay_Status"]].head(10))


# ==================================================================================================
# QUERY() EXAMPLES
# ==================================================================================================

print("\n" + "-" * 100)
print("QUERY EXAMPLES")
print("-" * 100)


print("\nPassengers Older Than 60 Years")

senior = df.query("Age > 60")

print(senior.head())


print("\nBusiness Class Passengers")

business = df.query("Class == 'Business'")

print(business.head())


print("\nSatisfied Customers")

satisfied = df.query("satisfaction == 'satisfied'")

print(satisfied.head())


print("\nFlight Distance Greater Than 3000 KM")

long_distance = df.query("Flight_Distance > 3000")

print(long_distance.head())


# ==================================================================================================
# WHERE() EXAMPLE
# ==================================================================================================

print("\n" + "-" * 100)
print("WHERE() FUNCTION")
print("-" * 100)

df["Modified_Departure_Delay"] = df["Departure_Delay"].where(

    df["Departure_Delay"] <= 60,

    60

)

print(df[["Departure_Delay", "Modified_Departure_Delay"]].head(10))


# ==================================================================================================
# MASK() EXAMPLE
# ==================================================================================================

print("\n" + "-" * 100)
print("MASK() FUNCTION")
print("-" * 100)

df["Modified_Arrival_Delay"] = df["Arrival_Delay"].mask(

    df["Arrival_Delay"] > 60,

    60

)

print(df[["Arrival_Delay", "Modified_Arrival_Delay"]].head(10))


# ==================================================================================================
# GROUPBY() + AGG()
# ==================================================================================================

print("\n" + "-" * 100)
print("AGE GROUP ANALYSIS")
print("-" * 100)

age_analysis = df.groupby("Age_Group").agg({

    "Flight_Distance": ["mean", "max", "min"],

    "Departure_Delay": ["mean", "max"],

    "Arrival_Delay": ["mean", "max"]

}).round(2)

print(age_analysis)


# ==================================================================================================
# SATISFACTION BY AGE GROUP
# ==================================================================================================

print("\n" + "-" * 100)
print("SATISFACTION BY AGE GROUP")
print("-" * 100)

age_satisfaction = (

    df.groupby("Age_Group")["satisfaction"]

      .value_counts()

)

print(age_satisfaction)


# ==================================================================================================
# DELAY STATUS DISTRIBUTION
# ==================================================================================================

print("\n" + "-" * 100)
print("DELAY STATUS DISTRIBUTION")
print("-" * 100)

print(df["Delay_Status"].value_counts())


# ==================================================================================================
# SUMMARY REPORT
# ==================================================================================================

print("\n" + "=" * 100)
print("ADVANCED PANDAS SUMMARY REPORT")
print("=" * 100)

print(f"Total Adults                  : {(df['Age_Group'] == 'Adult').sum()}")

print(f"Total Teenagers               : {(df['Age_Group'] == 'Teen').sum()}")

print(f"Total Children                : {(df['Age_Group'] == 'Child').sum()}")

print(f"Total Senior Citizens         : {(df['Age_Group'] == 'Senior').sum()}")

print()

print(f"On-Time Flights               : {(df['Delay_Status'] == 'On Time').sum()}")

print(f"Minor Delay Flights           : {(df['Delay_Status'] == 'Minor Delay').sum()}")

print(f"Major Delay Flights           : {(df['Delay_Status'] == 'Major Delay').sum()}")


# ==================================================================================================
# BUSINESS INSIGHTS
# ==================================================================================================

print("\n" + "=" * 100)
print("BUSINESS INSIGHTS")
print("=" * 100)

print("""

1. Age groups have been created using apply().

2. Delay categories have been created using apply().

3. query() has been used to filter important passenger groups.

4. where() has been used to cap departure delays.

5. mask() has been used to modify arrival delays.

6. groupby() and agg() have been used for age-wise analysis.

7. Customer satisfaction has been analyzed for each age group.

""")


# ==================================================================================================
# MODULE COMPLETION
# ==================================================================================================

print("=" * 100)
print("MODULE 7 COMPLETED SUCCESSFULLY")
print("=" * 100)
# ==================================================================================================
#                                        MODULE 8
#                     DATAFRAME COMBINATION & RESHAPING OPERATIONS
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Project Objective
# --------------------------------------------------------------------------------------------------
# This module demonstrates how to combine multiple DataFrames
# using merge(), join(), concat(), and stack().
# --------------------------------------------------------------------------------------------------


print("\n" + "=" * 100)
print("DATAFRAME COMBINATION & RESHAPING")
print("=" * 100)


# ==================================================================================================
# CREATE AIRLINE INFORMATION DATAFRAME
# ==================================================================================================

print("\n" + "-" * 100)
print("AIRLINE INFORMATION DATAFRAME")
print("-" * 100)

airline_info = pd.DataFrame({

    "Class": ["Business", "Eco", "Eco Plus"],

    "Ticket_Price": [15000, 7000, 10000],

    "Lounge_Access": ["Yes", "No", "Limited"]

})

print(airline_info)


# ==================================================================================================
# MERGE()
# ==================================================================================================

print("\n" + "-" * 100)
print("MERGE() EXAMPLE")
print("-" * 100)

merged_df = pd.merge(

    df,

    airline_info,

    on="Class",

    how="left"

)

print(merged_df.head())


print("\nMerged Dataset Shape :", merged_df.shape)


# ==================================================================================================
# CREATE AIRPORT DATAFRAME
# ==================================================================================================

print("\n" + "-" * 100)
print("AIRPORT INFORMATION")
print("-" * 100)

airport = pd.DataFrame({

    "Airport": ["Delhi", "Mumbai", "Bangalore"],

    "Airport_Code": ["DEL", "BOM", "BLR"]

})

airport.index = [0, 1, 2]

print(airport)


# ==================================================================================================
# JOIN()
# ==================================================================================================

print("\n" + "-" * 100)
print("JOIN() EXAMPLE")
print("-" * 100)

joined_df = airline_info.join(airport)

print(joined_df)


# ==================================================================================================
# CONCAT()
# ==================================================================================================

print("\n" + "-" * 100)
print("CONCAT() EXAMPLE")
print("-" * 100)

business_class = df[df["Class"] == "Business"].head(5)

eco_class = df[df["Class"] == "Eco"].head(5)

combined_df = pd.concat(

    [business_class, eco_class],

    ignore_index=True

)

print(combined_df)

print("\nCombined Dataset Shape :", combined_df.shape)


# ==================================================================================================
# STACK()
# ==================================================================================================

print("\n" + "-" * 100)
print("STACK() EXAMPLE")
print("-" * 100)

sample = pd.DataFrame({

    "Service": ["Seat Comfort", "WiFi", "Food"],

    "Rating": [4, 3, 5]

})

print("\nOriginal DataFrame\n")

print(sample)

print("\nStacked Data\n")

stacked_data = sample.stack()

print(stacked_data)


# ==================================================================================================
# SUMMARY REPORT
# ==================================================================================================

print("\n" + "=" * 100)
print("DATAFRAME OPERATIONS SUMMARY")
print("=" * 100)

print(f"Original Dataset Rows          : {df.shape[0]}")

print(f"Merged Dataset Rows            : {merged_df.shape[0]}")

print(f"Merged Dataset Columns         : {merged_df.shape[1]}")

print(f"Joined Dataset Rows            : {joined_df.shape[0]}")

print(f"Joined Dataset Columns         : {joined_df.shape[1]}")

print(f"Concatenated Dataset Rows      : {combined_df.shape[0]}")

print(f"Concatenated Dataset Columns   : {combined_df.shape[1]}")

print(f"Stacked Data Size              : {len(stacked_data)}")


# ==================================================================================================
# BUSINESS INSIGHTS
# ==================================================================================================

print("\n" + "=" * 100)
print("BUSINESS INSIGHTS")
print("=" * 100)

print("""

1. merge() combines passenger data with airline information
   using the common 'Class' column.

2. join() combines DataFrames using their indexes.

3. concat() combines Business and Eco passenger records
   into a single DataFrame.

4. stack() converts columns into rows, making the data
   suitable for hierarchical analysis.

5. These functions are widely used in real-world data
   engineering and analytics projects.

""")


# ==================================================================================================
# MODULE COMPLETION
# ==================================================================================================

print("=" * 100)
print("MODULE 8 COMPLETED SUCCESSFULLY")
print("=" * 100)

# ==================================================================================================
#                                        MODULE 9
#                            FINAL BUSINESS REPORT & CONCLUSION
# ==================================================================================================

# --------------------------------------------------------------------------------------------------
# Project Objective
# --------------------------------------------------------------------------------------------------
# This module summarizes all the important insights obtained
# from the airline dataset and generates a professional
# business report.
# --------------------------------------------------------------------------------------------------


print("\n" + "=" * 100)
print("                     FINAL AIRLINE CUSTOMER SATISFACTION REPORT")
print("=" * 100)


# ==================================================================================================
# GENERAL INFORMATION
# ==================================================================================================

print("\n" + "-" * 100)
print("GENERAL INFORMATION")
print("-" * 100)

print(f"Total Passengers                  : {df.shape[0]}")

print(f"Total Features                    : {df.shape[1]}")

print(f"Average Passenger Age             : {round(df['Age'].mean(),2)} Years")

print(f"Youngest Passenger                : {df['Age'].min()} Years")

print(f"Oldest Passenger                  : {df['Age'].max()} Years")

print(f"Average Flight Distance           : {round(df['Flight_Distance'].mean(),2)} Km")

print(f"Maximum Flight Distance           : {df['Flight_Distance'].max()} Km")

print(f"Minimum Flight Distance           : {df['Flight_Distance'].min()} Km")


# ==================================================================================================
# CUSTOMER SATISFACTION REPORT
# ==================================================================================================

print("\n" + "-" * 100)
print("CUSTOMER SATISFACTION REPORT")
print("-" * 100)

print(df["satisfaction"].value_counts())

print("\nPercentage Distribution")

print(round(df["satisfaction"].value_counts(normalize=True) * 100, 2))


# ==================================================================================================
# CUSTOMER TYPE REPORT
# ==================================================================================================

print("\n" + "-" * 100)
print("CUSTOMER TYPE REPORT")
print("-" * 100)

print(df["Customer_Type"].value_counts())


# ==================================================================================================
# TRAVEL TYPE REPORT
# ==================================================================================================

print("\n" + "-" * 100)
print("TRAVEL TYPE REPORT")
print("-" * 100)

print(df["Travel_Type"].value_counts())


# ==================================================================================================
# TRAVEL CLASS REPORT
# ==================================================================================================

print("\n" + "-" * 100)
print("TRAVEL CLASS REPORT")
print("-" * 100)

print(df["Class"].value_counts())


# ==================================================================================================
# SERVICE QUALITY REPORT
# ==================================================================================================

print("\n" + "-" * 100)
print("SERVICE QUALITY REPORT")
print("-" * 100)
print(average_rating.sort_values(ascending=False))

print(f"Service Name : {average_rating.idxmax()}")

print(f"Average Rating : {average_rating.max()}")

print(f"Service Name : {average_rating.idxmin()}")

print(f"Average Rating : {average_rating.min()}")

print()

# print("Best Rated Service")

# print(f"Service Name                     : {service_rating.idxmax()}")

# print(f"Average Rating                   : {service_rating.max()}")

# print()

# print("Lowest Rated Service")

# print(f"Service Name                     : {service_rating.idxmin()}")

# print(f"Average Rating                   : {service_rating.min()}")


# ==================================================================================================
# DELAY REPORT
# ==================================================================================================

print("\n" + "-" * 100)
print("FLIGHT DELAY REPORT")
print("-" * 100)

print(f"Average Departure Delay          : {round(df['Departure_Delay'].mean(),2)} Minutes")

print(f"Average Arrival Delay            : {round(df['Arrival_Delay'].mean(),2)} Minutes")

print(f"Maximum Departure Delay          : {df['Departure_Delay'].max()} Minutes")

print(f"Maximum Arrival Delay            : {df['Arrival_Delay'].max()} Minutes")


# ==================================================================================================
# AGE GROUP REPORT
# ==================================================================================================

print("\n" + "-" * 100)
print("AGE GROUP REPORT")
print("-" * 100)

print(df["Age_Group"].value_counts())


# ==================================================================================================
# DELAY STATUS REPORT
# ==================================================================================================

print("\n" + "-" * 100)
print("DELAY STATUS REPORT")
print("-" * 100)

print(df["Delay_Status"].value_counts())


# ==================================================================================================
# TOP 10 MOST DELAYED FLIGHTS
# ==================================================================================================

print("\n" + "-" * 100)
print("TOP 10 DEPARTURE DELAYS")
print("-" * 100)

print(df.sort_values(

    by="Departure_Delay",

    ascending=False

).head(10)[

    ["Customer_Type",

     "Travel_Type",

     "Class",

     "Departure_Delay"]

])


print("\nTop 10 Arrival Delays")

print(df.sort_values(

    by="Arrival_Delay",

    ascending=False

).head(10)[

    ["Customer_Type",

     "Travel_Type",

     "Class",

     "Arrival_Delay"]

])


# ==================================================================================================
# FINAL BUSINESS INSIGHTS
# ==================================================================================================

print("\n" + "=" * 100)
print("FINAL BUSINESS INSIGHTS")
print("=" * 100)

print("""

1. The airline dataset was successfully cleaned and analyzed.

2. Missing values and duplicate records were handled properly.

3. Customer satisfaction was analyzed based on:
      • Customer Type
      • Travel Type
      • Travel Class

4. Flight Distance and Delay patterns were analyzed.

5. Airline services were ranked from best to worst.

6. Delay trends were analyzed using:
      • Customer Type
      • Travel Type
      • Travel Class

7. Advanced Pandas operations such as
      • apply()
      • query()
      • where()
      • mask()
      • groupby()
      • agg()
      • merge()
      • join()
      • concat()
      • stack()
   were successfully implemented.

8. A final business report was generated to support
   data-driven decision making.

""")


# ==================================================================================================
# RECOMMENDATIONS
# ==================================================================================================

print("\n" + "=" * 100)
print("BUSINESS RECOMMENDATIONS")
print("=" * 100)

print("""

✓ Improve the lowest-rated airline service.

✓ Reduce departure and arrival delays.

✓ Focus on improving passenger satisfaction in lower-rated travel classes.

✓ Enhance customer experience through better onboard services.

✓ Monitor delay trends regularly to improve operational efficiency.

✓ Continue collecting customer feedback for service improvement.

""")


# ==================================================================================================
# PROJECT SUMMARY
# ==================================================================================================

print("\n" + "=" * 100)
print("PROJECT SUMMARY")
print("=" * 100)

print(f"Dataset Name                     : Airline Customer Satisfaction")

print(f"Total Records                    : {df.shape[0]}")

print(f"Total Features                   : {df.shape[1]}")

print(f"Programming Language             : Python")

print(f"Library Used                     : Pandas")

print()

print("Pandas Functions Demonstrated:")

print("""

✔ read_csv()

✔ head()

✔ tail()

✔ shape

✔ columns

✔ dtypes

✔ info()

✔ describe()

✔ isnull()

✔ fillna()

✔ duplicated()

✔ drop_duplicates()

✔ rename()

✔ to_numeric()

✔ value_counts()

✔ groupby()

✔ agg()

✔ apply()

✔ query()

✔ where()

✔ mask()

✔ merge()

✔ join()

✔ concat()

✔ stack()

✔ sort_values()

✔ idxmax()

✔ idxmin()

✔ mean()

✔ max()

✔ min()

✔ round()

""")


# ==================================================================================================
# PROJECT COMPLETION
# ==================================================================================================

print("=" * 100)
print("           AIRLINE CUSTOMER SATISFACTION ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 100)

print("\nThank You for Using This Project.")

print("\nAuthor : Shivansh Chaurasiya")