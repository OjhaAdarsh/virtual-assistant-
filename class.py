def putNumbers(n):

    i = 0

    while i<=n:

        j=i

        i=i+1

        if j%7==0:

            yield j


num=int(input("Enter the number"))
for i in putNumbers(num):

    print (i)