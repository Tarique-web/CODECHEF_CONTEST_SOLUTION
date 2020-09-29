# -----------------------SMART PHONE----------------------
test_cases=int(input())
budget=[]
for i in range(test_cases):
	budget.append(int(input()))
budget.sort()
budget_len=len(budget)
budget_max=[]
for j in range(budget_len):
	budget_max.append((budget[j]*(budget_len)))	
	budget_len-=1
max1=budget_max[0]
for l in range(len(budget_max)):
	if budget_max[l]>=max1:
		max1=budget_max[l]
print(max1)

# ----------------------------Grade The Steel-------------------------------------
TestCase=int(input())
for i in range(TestCase):
	H,C,T=map(str,input().split())
	H=int(H)
	C=float(C)
	T=int(T)
	if H>50 and C<0.7 and T>5600:
	    grade=10
	elif H>50 and C<0.7:
	    grade=9
	elif C<0.7 and T>5600:
	    grade=8
	elif H>50 and T>5600:
	    grade=7
	elif H>50 or C<0.7 or T>5600:
 	    grade=6
	else:
	    grade=5
	print(grade)

# -----------------------Chef and Remissness --------------------
TestCase=int(input())
for i in range(TestCase):
    A,B=map(int,input().split())
    if A>B:
        print(A,A+B)
    else:
        print(B,A+B)

 # --------------------------Lucky Fours-----------------------
TestCase=int(input())
for i in range(TestCase):
    N=input()
    counter=0
    for j in range(0,len(N)):
        if N[j]=="4":
            counter+=1
    print(counter)

# ---------------------------------------------------------TEST DONE BY 28SEP2020----------------------------------------------------------------------