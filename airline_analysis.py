"""
Airline Customer Satisfaction Analysis
GitHub-ready starter (single file)
"""

import pandas as pd

def load_dataset(path):
    return pd.read_csv(path)

def clean_data(df):
    df["Arrival Delay in Minutes"] = df["Arrival Delay in Minutes"].fillna(
        df["Arrival Delay in Minutes"].mean()
    )
    df.drop_duplicates(inplace=True)
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
    df["Departure_Delay"] = pd.to_numeric(df["Departure_Delay"], errors="coerce")
    return df

def main():
    df = load_dataset("airline.csv")
    df = clean_data(df)

    print("="*70)
    print("AIRLINE CUSTOMER SATISFACTION ANALYSIS")
    print("="*70)

    print("Total Passengers:", df.shape[0])
    print("Average Age:", round(df["Age"].mean(),2))
    print("Youngest:", df["Age"].min())
    print("Oldest:", df["Age"].max())

    print("\nCustomer Types")
    print(df["Customer_Type"].value_counts())

    print("\nTravel Types")
    print(df["Travel_Type"].value_counts())

    print("\nClass")
    print(df["Class"].value_counts())

    print("\nSatisfaction")
    print(df["satisfaction"].value_counts())

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

    print("\nService Ratings")
    print(df[services].mean().round(2).sort_values(ascending=False))

    print("\nDelay Report")
    print(df.groupby("satisfaction").agg({
        "Departure_Delay":["mean","max","min"],
        "Arrival_Delay":["mean","max","min"]
    }))

    print("\nCompleted Successfully")

if __name__ == "__main__":
    main()
