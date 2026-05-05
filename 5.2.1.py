import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset from the CSV file
df = pd.read_csv('titanic.csv')

# Set up the figure for 5 subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 12))

# write the code..
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset from the CSV file
df = pd.read_csv('titanic.csv')

# Set up the figure for 5 subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 12))

# write the code..
#plot 1: Count of passenger by class
axes[0,0].bar(df['Pclass'].value_counts().index,
			  df['Pclass'].value_counts(),color='skyblue')
axes[0,0].set_title("Passenger Class Distribution")
axes[0,0].set_xlabel("Pclass")
axes[0,0].set_ylabel("Count")

#plot 2: Gender Distribution
axes[0,1].pie(df['Gender'].value_counts(),labels=df['Gender'].value_counts().index,autopct='%1.1f%%',colors=['lightblue','lightcoral'])
axes[0,1].set_title("Gender Distribution")

#plot 3: Age Distribution
axes[1,0].hist(df['Age'].dropna(),bins=8,color='lightgreen',edgecolor='black')
axes[1,0].set_title("Age Distribution")
axes[1,0].set_xlabel("Age")
axes[1,0].set_ylabel("Frequency")
plt.show()