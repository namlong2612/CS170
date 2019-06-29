## examples of sequences 
## even intergeres from 2 through 34 , inclusive

for i in range (2, 34 +1, 2):
    print (i, end = "  ")
    
print()

for n in range (1, 17 +1):
    print(2**n, end ="  ")
    
print()

for n in range (0, 200 +1):
    print (2**n, end = "   ")
    
#print the terms of the sequence given by
# s_n = 3n +2n**2
#for n = 0, 1 , 2, ..., 40

for n in range (0, 40+1, 1):
    sn = 3*n + 2*(n**2)
    print(n, sn)
    
#print the first 11 terms of the sequence given by
#t_n = 3*n**2 - 2**n
#starting with n = -5
stop = -5 +11
line = 1
for n in range (-5, stop, 1):
    tn = 3*n**2 - 2**n
    print (line, tn)
    line = line +1
    
#inductive definition

# t_1 =3
# t_n = 4 * t_n-1

t1=3
print(t1)
tnMinus1 = t1 ## initial value
for n in range (2, 20 +1):
    tn =4*tnMinus1
    print(n, tn)
    tnMinus1 = tn # set up for next iteration
    
    

    
    

    