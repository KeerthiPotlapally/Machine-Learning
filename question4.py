#Question 4 :

it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A = {19,22,24,20,25,26}
B ={19,22,20,25,26,24,28,27}
age = [22,19,24,25,26,24,25,24]

#Find the length of the set it_companies 
print("Length of the it_compaines set is :",len(it_companies))

#Add "Twitter" to it_companies 
it_companies.add("Twitter")
print("Twitter added to it_compaines set :",it_companies)

#insert multiple IT Companies at once to the set 
itc = {"Wipro","TCS"}
it_companies.update(itc)
print("inserting multiple IT Companies at once to the set :",it_companies)

# Remove one of the compaines from the set 
it_companies.remove("Apple")
print("Remove one of the compaines from the set :",it_companies)

#Join A and B
print("Join Set :", A.union(B))

#Find A intersection B
print("A intersection B :", A.intersection(B))

# Is A subset of B
print("Is A subset of B :", A.issubset(B))

# Are A and B disjoint sets
print("Are A and B disjoint sets :", A.isdisjoint(B))

# Join A with B and B with A
print("Join A with B :", A.union(B))
print("Join b with A :", B.union(A))

#What is the symmetric difference between A and B
print("symmetric difference between A and B :", A.symmetric_difference(B))

#Delete the sets completely
del it_companies
del A
del B

#Convert the ages to a set and compare the length of the list and the set.

listlength = len(age)
print("Length of the ages list :", listlength)
Setages = set(age)
Setlength = len(Setages)
print("Length of the ages set :", Setlength)

if ( listlength == Setlength ):
   print ("Line 1 - listlength is equal to Setlength")
else:
   print ("Line 1 - listlength is not equal to Setlength")

if ( listlength != Setlength ):
   print ("Line 2 - listlength is not equal to Setlength")
else:
   print ("Line 2 - listlength is equal to Setlength")

if ( listlength < Setlength ):
   print ("Line 3 - listlength is less than Setlength" )
else:
   print ("Line 3 - listlength is not less than Setlength")

if ( listlength > Setlength ):
   print ("Line 4 - listlength is greater than Setlength")
else:
   print ("Line 4 - listlength is not greater than Setlength")
