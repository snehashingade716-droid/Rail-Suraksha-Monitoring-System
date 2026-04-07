import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("railway_complaints.csv")

# Show data
print("First 5 rows:")
print(df.head())

# Complaint count
print("\nComplaint Types:")
print(df['Complaint_Type'].value_counts())

# Location count
print("\nTop Locations:")
print(df['Location'].value_counts())

# Convert time to hour
df['Hour'] = pd.to_datetime(df['Time']).dt.hour

# Night complaints
night = df[df['Hour'] > 20]
print("\nNight Complaints:")
print(night['Location'].value_counts())

# Plot graph
df['Complaint_Type'].value_counts().plot(kind='bar')
plt.title("Complaint Types")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()