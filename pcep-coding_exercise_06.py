# Coding Exercise 6: Python Guessing Game
#
# Scenario:
#
# Ask the user to guess the year when Python 1.0 was released (the correct answer is 1994) with the following prompt:
#
# When was Python 1.0 released? << remember to add a space at the end of this prompt
#
# If the user answers 1994, show:
#
# Correct!
#
# and finish the program. If the user answers with any year that is later than 1994, show a hint and ask again for a new year on a new line:
#
# It was earlier than that!
# When was Python 1.0 released? << remember to add a space
#
# If the user answers with any year that is earlier than 1994, show a hint and ask again for a new year on a new line:
#
# It was later than that!
# When was Python 1.0 released? << remember to add a space

while True:
    year = int(input('When was Python 1.0 released? '))
    if year < 1994:
        print('It was later than that!')
        continue
    elif (year > 1994):
        print('It was earlier than that!')
        continue
    else:
        print('Correct!')
        break
