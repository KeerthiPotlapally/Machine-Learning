#Question 3

# Create  a tuple containing names of sisters and brothers 
Brothers = ('vivek','Ajay','Ajit')
Sisters = ('Tinku','Teja')
print("Names of Brothers: ", Brothers)
print("Names of Sisters: ", Sisters)

# Join sisters,brothers tuple and assign it to siblings 
Siblings = Brothers + Sisters
print("Names of Siblings: ",Siblings)

#How many siblings do you have 
print("Number of siblings: ", len(Siblings))

#Modify the siblings tuple and add the name of Mother and Father 
family_members = Siblings + ('Hymavathi', 'Sripathi Rao', )
print("Family Members: ", family_members)