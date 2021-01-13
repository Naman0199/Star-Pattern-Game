print("Pattern Game")
n = int(input("enter the number of rows for patterns:\n"))
b = bool(int(input("enter 1 for True  or 0 for False:\n")))
if b==1:
    c = 0
    while(c<=n):
        print("*"*c)
        c = c+1

elif b==0:
    c=n
    while(c>0):
        print("*"*c)
        c = c-1

else:
    print("enter valid pattern")



