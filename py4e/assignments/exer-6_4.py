# using a while loop to display the contents of a string backwards
# len() find the length of a variable, while [-1] picks the last letter

her = 'someone to love'

ella = 0
while ella < len(her) : 
    puzzle = her[ella - 1]
    ella = ella + 1
    print(puzzle, ella)

