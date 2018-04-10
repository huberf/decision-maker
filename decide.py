introduction = 'This utility requires you have two clearly defined options.'
print(introduction)
optionA = input('Option A> ')
optionB = input('Option B> ')
print('Now I will ask you for the advantages and disadvantages of "' + optionA + '"')
advantagesA = input('Advantages A> ')
disadvantagesA = input('Disadvantages A> ')
print('Now I will ask you for the advantages and disadvantages of "' + optionB + '"')
advantagesB = input('Advantages B> ')
disadvantagesB = input('Disadvantages B> ')
print('')
print('Now you will rank the tradeoff between A and B on a scale between 1 and 100 where the sum is always 100.')
print("Rank advantages of A vs B")
print('A: ' + advantagesA)
print('B: ' + advantagesB)
notGood = True
box5 = 0
box6 = 0
while notGood:
    box5 = int(input('A> '))
    box6 = 100 - box5
    print('So is it A: ', box5, ' and B: ', box6, '? [y/n]')
    if input('> ') == 'y':
        notGood = False
print('')
print("Rank disadvantages of A vs B [higher = worse]")
print('A: ' + disadvantagesA)
print('B: ' + disadvantagesB)
notGood = True
box7 = 0
box8 = 0
while notGood:
    box7 = int(input('A> '))
    box8 = 100 - box7
    print('So is it A: ', box7, ' and B: ', box8, '? [y/n]')
    if input('> ') == 'y':
        notGood = False
print('')
print("Rank advantages of A vs disadvantages of A")
print('Advantages: ' + advantagesA)
print('Disadvantages: ' + disadvantagesA)
notGood = True
box1 = 0
box2 = 0
while notGood:
    box1 = int(input('Advantage> '))
    box2 = 100 - box1
    print('So is it advantage: ', box1, ' and disadvantage: ', box2, '? [y/n]')
    if input('> ') == 'y':
        notGood = False
print('')
print("Rank advantages of B vs disadvantages of B")
print('Advantages: ' + advantagesB)
print('Disadvantages: ' + disadvantagesB)
notGood = True
box3 = 0
box4 = 0
while notGood:
    box3 = int(input('Advantage> '))
    box4 = 100 - box3
    print('So is it advantage: ', box3, ' and disadvantage: ', box4, '? [y/n]')
    if input('> ') == 'y':
        notGood = False
print('')
box9 = box5 + box1
box11 = box3 + box6
box10 = box2 + box7
box12 = box4 + box8
finalA = box9 - box10
finalB = box11 - box12
if finalA > 0 and finalB > 0:
    if finalA > finalB:
        print('Both choices are solid options but A is slightly better')
    else:
        print('Both choices are solid options but B is slightly better')
elif finalA < 0 and finalB < 0:
    print('Both options are negatives. This is shown to be a symptom of a depressed mindset.')
    if finalA > finalB:
        print('Option A is best though')
    elif finalA < finalB:
        print('Option B is best though')
    else:
        print('Both are tied.')
else:
    if finalA > finalB:
        print('Option A is best')
    elif finalA < finalB:
        print('Option B is best')
    else:
        print('Both are tied')
