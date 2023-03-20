# prompt the user for a score between 0 and 1 and print the associated grade.

score = input('Enter your score\n')
convert_score = float(score)

if convert_score >= 0.9 and convert_score <  1.0 :
    print('A')
elif convert_score < 0.9 and convert_score >= 0.8 :
    print('B')
elif convert_score < 0.8 and convert_score >= 0.7 :
    print('C')
elif convert_score < 0.7 and convert_score >= 0.6 :
    print('D')
elif convert_score < 0.6 :
    print('F')
else :
    print('Please enter a valid decimal')                