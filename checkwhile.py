def checkwhile(i):
    count=0
    while i > 10:
        i-=1
        print(i)
        count+=1
    print("total count is: ", count)

c=checkwhile(20)
print(c)