#Question 1
ages = [19,22,19,24,20,25,26,24,25,24]
print("The given list is : ", ages)

#Sorting the list 
ages.sort()
print("The Sorted list is : ", ages)

#Min age from the list 
minage = min(ages)
print("The Min age from the list is : ", minage)

#Max age from the list 
maxage = max(ages)
print("The Max age from the list is : ", maxage)

#appending Min age and Max age to the given list 
ages.append(minage)
ages.append(maxage)
print("The List after appending Min age and Max Age : ", ages)

#Finding median age from the list 
ages.sort()
if len(ages) % 2 == 0:
   first_median = ages[len(ages)// 2]
   second_median = ages[len(ages)// 2 - 1]
   median = (first_median + second_median) / 2
else:
   median = ages[len(ages)]
print("Median of above list is: " + str(median))

#Finding Average age from the list 
def calc_average(avgages):  
    return sum(ages) / len(ages)  
avgages = ages  
average = calc_average(avgages)
print("The average of the list is ", round(average, 3)) 

#Finding Range of the list 
minage = min(ages)
maxage = max(ages)
Rangeofages = max(ages) - min(ages)
print("The Range of the list is ", Rangeofages)