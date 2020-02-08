basic,grade=input().split()
basic=int(basic)
grade=str(grade)
#grade=str(input())
# totalSalary = basic + hra + da + allow – pf
# hra   = 20% of basic
# da    = 50% of basic
# allow = 1700 if grade = ‘A’
# allow = 1500 if grade = ‘B’
# allow = 1300 if grade = ‘C' or any other character
# pf    = 11% of basic.

allow=0
hra=0.2*basic
da=0.5*basic
pf=0.11*basic
if grade=='A':
    allow=1700
elif grade=='B':
    aloow=1500
else:
    allow=1300
totalSalary = basic+hra+da+allow-pf
print(int(totalSalary))  
