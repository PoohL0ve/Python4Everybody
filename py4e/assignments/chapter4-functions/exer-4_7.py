# Using a function to return scores

score = input('Please enter your score:\n')
convert_score = float(score)

def computegrade(convert_score) : 
    if convert_score >= 0.9 and convert_score < 1.0 :
        grade = 'A'
        return grade
    elif convert_score >= 0.8 and convert_score < 0.9 :
        grade = 'B'
        return grade
    elif convert_score >= 0.7 and convert_score < 0.8 :
        grade = 'C'
        return grade
    elif convert_score >= 0.6 and convert_score < 0.7 :
        grade = 'D'
        return grade
    elif convert_score >= 0.0 and convert_score < 0.6 :
        grade = 'F'
        return grade 
    else :
        print('Bad score, please enter values between 0.0 and 1.0')
test_score = computegrade(convert_score)
print('Your score:', test_score)