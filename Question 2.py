#Question 2 

# Create an empty dictionary called dog 
dog = {}

# Add Name, Colour, breed, legs, age to the dog dictionary 
dog = {'Colour':'Black', 'breed' : 'Pug', 'legs' : 4, 'age' : 10}

# Create a student dictionary  
student  = {}

# Add first_name,last_name,gender,age,material status,skills,country,city,address to  dictionary 
student  = {'first_name' : 'Keerthi','last_name' : 'Potlapally', 'gender' : 'Female', 'age' : 24, 'material status': 'Not Married','skills': ['Python','Java','SQL'], 'country' : 'India', 'City' : 'Hyderabad', 'Address' : {'H:No' : 101, 'Area' : 'Rcpuram'} }

# get length of the student dictionary 
print("Length of dictionary:",len(student))

# get the values the skills 
Skill_list = student.get('skills')
print("the values the skills : ", Skill_list)
# and check the data type 
print("the data type of the skills : ", type(Skill_list))
print("the data type of the First skill: ", type(Skill_list[0]))
print("the data type of the Second skill: ", type(Skill_list[1]))
print("the data type of the Third skill: ", type(Skill_list[2]))

# Modify the skills value by adding one or two skills 
student['skills'].append('HTML')
print("The Modified dictionary after adding skills :", student)

# Get dictionary key as the list 
print("The dictionary keys as the list :", list(student.keys()))

# Get dictionary values as the list 
print("The dictionary Values as the list :", list(student.values()))