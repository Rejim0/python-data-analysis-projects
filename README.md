🏋️ Gym Workout Data Analysis (Python)
📌 Project Overview
This project analyzes gym workout data using Python, Pandas, NumPy, and Matplotlib to uncover patterns related to workout types, calories burned, heart rate, workout duration, age distribution, and fitness levels.
The project focuses on real-world data analysis workflow, including:
Data loading and inspection
Data cleaning and preprocessing
Statistical analysis using NumPy
Data visualization using Matplotlib
This project is part of my learning journey in data analytics and Python programming.

📊 Dataset Description
The dataset (gymdata.csv) contains information about gym users and their workout habits, including:
UserID
Age
Gender
Weight (kg)
Workout Type
Workout Duration (minutes)
Calories Burned
Average Heart Rate
Workout Frequency
Fitness Level

🛠 Tools & Technologies Used
Python
Pandas
NumPy
Matplotlib
CSV file handling

📂 Project Structure
python-data-analysis-projects/
│
├── Gym_Project.py                 # Main Python analysis script
├── gymdata.csv                    # Dataset
├── scatter_calories_vs_duration.png
├── bar_avg_calories_by_workout.png
├── pie_workout_distribution.png
├── hist_age_distribution.png
├── gym_dashboard.png              # Combined subplot dashboard
└── README.md                      # Project documentation

🔍 Key Analysis Performed
Loaded and inspected CSV data using Pandas
Checked data types, duplicates, and summary statistics
Cleaned inconsistent text data (case and spacing)
Handled missing values using statistical methods
Converted Pandas data to NumPy arrays for numerical analysis
Calculated:
Mean, min, max, and standard deviation
Correlation between workout duration and calories burned
Grouped data to analyze calories burned by:
Workout type
Fitness level

📈 Data Visualizations (Matplotlib)
The project includes multiple visualizations:
Scatter Plot: Workout Duration vs Calories Burned
Bar Chart: Average Calories Burned by Workout Type
Pie Chart: Workout Type Distribution
Histogram: Age Distribution of Gym Users
Subplot Dashboard: Combined view of all visualizations
All plots are saved as .png files for documentation and portfolio use.
