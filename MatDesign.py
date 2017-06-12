N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted. 9 27
for i in range(1,N,2): # 1, 3, 5, 7
    #print ("-" * ((M-(i * 3))/2)) + (".|." * i) + ("-" * ((M-(i * 3))/2))
    print (str(".|." * i)).center(M, '-')
print ("-" * ((M-7)/2)) + "WELCOME" + ("-" * ((M-7)/2))
for i in range(N-2,-1,-2): # 7, 5, 3, 1
    #print ("-" * ((M-(i * 3))/2)) + (".|." * i) + ("-" * ((M-(i * 3))/2))
    print (str(".|." * i)).center(M, '-')
