
score = input('Enter score :')
nscore = float(score)

if nscore < 0.6 :
    print('F')
elif nscore >= 0.6 and nscore < 0.7 :
    print('D')
elif nscore >= 0.7 and nscore < 0.8 :
    print('C')
elif nscore >= 0.8 and nscore < 0.9 :
    print('B')
elif nscore >= 0.9 and nscore < 1.0 :
    print('A')
else :
    print('Not applicable')

# Good use of the and 