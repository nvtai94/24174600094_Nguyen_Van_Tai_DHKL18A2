#bai_3
#Số cần in
n = 50

#Hai số đầu trong dãy Fibonacci
a, b = 0, 1

#In 50 số Fibonacci
for i in range(n):
    print(a, end=" ")  
    a, b = b, a + b  


