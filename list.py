def add(A,B,m,m):
    size= max(m,n)
    sum=[0 for i in range(size)]
    for i in range(m):
        sum[i]=A[i]
        for i in range (n):
            sum[i]+=B[i]
        return sum
    def printpoly(poly,n):
      for i in range(n):
          print(poly[i], end=" ")
          if i !=0:
             print("x^",i,end=" ")
             if i != n-1:
                   print("+", end=" ")
                   if_name_=="__main__":
                       A=[5,10,10,16]
                        B=[1,2,4]
                        m=len(A)
                         n-len(B)
                          print("first polynomial is")
                           printpoly(A,m)
                           print("\n", end="")
                           print("second polynomial is")
                           printpoly(B,n)
                           print("\n", end="")
                           sum=add(A,B,m,n)
                           size=max(m,n)
                          print("sum polynomial is")
                          print poly(sum,size)
              
