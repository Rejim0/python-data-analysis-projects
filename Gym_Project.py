import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("gymdata.csv")

# You must show:
# First 5 rows
# Data types
# Summary statistics
print("\nFirst Five Rows: ")
print(df.head().to_string())

print("\nData Types: ")
df.info()

print("\nSummary statistics: ")
print(df.describe().to_string())

#Check duplicates
print("\nDuplicate rows:", df.duplicated().sum())

# Fix inconsistent text
column_check = df.select_dtypes(include = "object")
df["Gender"] = df["Gender"].str.lower().str.strip()
df["Workout_Type"] = df["Workout_Type"].str.lower().str.strip()
df["Fitness_Level"] = df["Fitness_Level"].str.lower().str.strip()

# Handle missing values
df["Workout_Frequency"] = pd.to_numeric(df["Workout_Frequency"], errors = 'coerce')
number_check = df.select_dtypes(include = "number")
df["Workout_Frequency"] = df["Workout_Frequency"].fillna(df["Workout_Frequency"].mean())


# NumPy Statistics (IMPORTANT)
# Convert Pandas → NumPy

workoutDuration = df["Workout_Duration"].to_numpy()
caloriesBurned = df["Calories_Burned"].to_numpy()
heart_rate = df["Heart_Rate_Avg"].to_numpy()

print("\nAverage Calories: ", np.mean(caloriesBurned))
print("Max Calorie: ", caloriesBurned.max())
print("Min Calorie: ", caloriesBurned.min())
print("Std Dev Calories: ", caloriesBurned.std()) #Standard deviation = average distance from the mean

#Correlation tells you how strongly two things move together — not why.
correlation = np.corrcoef(workoutDuration, caloriesBurned)[0,1]
print("\nCorrelation between duration and calories:",correlation)

#Average calories by workout type
workoutTypeGroup = df.groupby("Workout_Type")
averageBurned_calorie = workoutTypeGroup["Calories_Burned"].mean()
print("\n",averageBurned_calorie)

#Calories by fitness level
FitnessLevelGroup = df.groupby("Fitness_Level")
average_calorie = FitnessLevelGroup["Calories_Burned"].mean()
print("\n",average_calorie)

# Most frequent workout type
most_common = df["Workout_Type"].value_counts()
print("\nWorkout Counts:\n",most_common)

# Create a scatter plot showing the relationship between workout duration and calories burned.
workoutDuration = df["Workout_Duration"]
caloriesBurned = df["Calories_Burned"]
plt.scatter(workoutDuration,caloriesBurned)
plt.xlabel("Workout Duration")
plt.ylabel("Calories Burned")
plt.title("Relation of Calorie and Workout Duration")
plt.grid(color = "blue", linestyle = "dashed")
plt.savefig("scatter_calories_vs_duration.png")
plt.show()


# Calculate the average calories burned for each workout type.
# Visualize the average calories by workout type using a bar chart.
# Customize the bar chart with:
# Proper labels
# Title
# Grid lines on one axis
plt.bar(averageBurned_calorie.index, averageBurned_calorie.values)
plt.title("Average Calories Burned Per Workout Type")
plt.xlabel("Workout Type")
plt.ylabel("Average Calorie")
plt.grid(axis = "y")
plt.savefig("bar_avg_calories_by_workout.png")
plt.show()

# Count how many users belong to each workout type.
# Display the workout type distribution using a pie chart.
# Customize the pie chart with:
# Percentage labels
# Start angle
# Clear title
plt.pie(most_common.values,labels = most_common.index, autopct = "%1.1f%%",startangle = 90, shadow = True)
plt.title("Workout Distribution Type")
plt.savefig("pie_workout_distribution.png")
plt.show()

# Plot a histogram to show the age distribution of gym users.
# Adjust the number of bins to better represent the data.
user_age = df["Age"].clip(18,60)
plt.hist(user_age, bins = 10)
plt.title("Age Distribution of gym Users")
plt.xlabel("Age")
plt.ylabel("Number of users")
plt.savefig("hist_age_distribution.png")
plt.show()

#Create a figure with multiple subplots (at least 4 plots in one figure).
# Place the following in a subplot layout:
# Scatter plot
# Bar chart
# Pie chart
# Histogram
# Add titles and axis labels to each subplot.
# Apply grid lines where appropriate in subplots.
# Adjust layout so plots do not overlap.
figure,axes = plt.subplots(2,2, figsize = (12,10))
axes[0,0].scatter(workoutDuration,caloriesBurned,alpha = 0.7)
axes[0,0].set_title("Scatter plot")
axes[0,0].set_xlabel("Workout Duration")
axes[0,0].set_ylabel("Calories Burned")
axes[0,0].grid()

axes[0,1].bar(averageBurned_calorie.index, averageBurned_calorie.values)
axes[0,1].set_title("Bar Chart")
axes[0,1].set_xlabel("Workout Type")
axes[0,1].set_ylabel("Average Calorie")
axes[0,1].grid(axis = "y")

axes[1,0].pie(most_common.values,labels = most_common.index, autopct = "%1.1f%%",startangle = 90, shadow = True)
axes[1,0].set_title("Workout Distribution Type")


axes[1,1].hist(user_age, bins = 10)
axes[1,1].grid()
axes[1,1].set_title("Age Distribution of gym Users")
axes[1,1].set_xlabel("Age")
axes[1,1].set_ylabel("Number of users")


plt.tight_layout()
figure.savefig("gym_dashboard.png")
plt.show()
