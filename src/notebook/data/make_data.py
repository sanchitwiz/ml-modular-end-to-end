import csv
import random

# Define the possible values for each category based on your sample
genders = ["Male", "Female"]
races = ["Group A", "Group B", "Group C", "Group D", "Group E"]
education_levels = ["High School", "Some College", "Associate's Degree", "College", "Master's Degree"]
lunch_options = ["Free", "Paid"]
test_prep_options = ["Completed", "Not Completed"]

# Create and open a new CSV file
with open('1000_students_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the exact header row you requested
    writer.writerow(["Gender", "Race_Ethnicity", "Parental_Education", "Lunch", "Test_Preparation_Course", "Math_Score", "Reading_Score", "Writing_Score"])
    
    # Generate 1,000 rows of randomized data
    for i in range(1, 1001):
        # student_id = i
        gender = random.choice(genders)
        race = random.choice(races)
        education = random.choice(education_levels)
        lunch = random.choice(lunch_options)
        test_prep = random.choice(test_prep_options)
        
        # Generate random scores between 40 and 100 to match your sample's distribution
        math_score = random.randint(40, 100)
        reading_score = random.randint(40, 100)
        writing_score = random.randint(40, 100)
        
        # Write the row
        writer.writerow([gender, race, education, lunch, test_prep, math_score, reading_score, writing_score])

print("File '1000_students_data.csv' has been generated successfully!")