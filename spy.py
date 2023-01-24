n=int(input())
sum=0
pr=1
for i in range(1,n+1):
    if n>0:
    d=n%10
    n=n//10
    sum=sum+d
    pr=pr*d
if sum==pr:
    print("Spy Number")
elif sum!=pr:
    print("Not Spy Number")
