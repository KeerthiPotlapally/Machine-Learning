# Online Python - IDE, Editor, Compiler, Interpreter
N = int(input("Enter the Number of the Students : "))
print(N);

Weight_in_LBS = []
Weight_in_KG = []

for i in range(N):
    txt = "Enter the weight of the {} student : "
    Weight_in_LBS.append(int(input((txt.format(i)))))
print("Weight in LBS : ", Weight_in_LBS)
 
for i in Weight_in_LBS:
    Weight_in_KG.append(i/2.2046)
    
print("Weight in KG : ", Weight_in_KG,3)