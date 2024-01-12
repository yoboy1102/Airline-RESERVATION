print()
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print(" \t \t \t \t \t \t \tWELCOME TO ABC")
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print()
dept=["ABC",'EFG','HIJ','LMN','OPQ']
nm=1
indept=0
for i in range(len(dept)):
    print(nm,'-' , dept[indept])
    indept+=1
    nm+=1
print()

e=int(input("ENTER YOU DEPARTURE POINT (BY THE NUMBER ASSIGNED TO IT):-- "))
if type(e)== int:
    if e<=len(dept):
        print("Your Departure point is;", dept[(e-1)],'\n Enter ee')