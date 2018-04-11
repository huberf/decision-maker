import ioutility as io
introduction = 'This utility requires you have two clearly defined options.'
io.put(introduction)
optionA = io.get('Option A> ')
optionB = io.get('Option B> ')
io.put('Now I will ask you for the advantages and disadvantages of "' + optionA + '"')
advantagesA = io.get('Advantages A> ')
disadvantagesA = io.get('Disadvantages A> ')
io.put('Now I will ask you for the advantages and disadvantages of "' + optionB + '"')
advantagesB = io.get('Advantages B> ')
disadvantagesB = io.get('Disadvantages B> ')
io.put('')
io.put('Now you will rank the tradeoff between A and B on a scale between 1 and 100 where the sum is always 100.')
io.put("Rank advantages of A vs B")
io.put('A: ' + advantagesA)
io.put('B: ' + advantagesB)
notGood = True
box5 = 0
box6 = 0
while notGood:
    box5 = io.getInt('A> ')
    box6 = 100 - box5
    io.put('So is it A: ', box5, ' and B: ', box6, '? [y/n]')
    if io.get('> ') == 'y':
        notGood = False
io.put('')
io.put("Rank disadvantages of A vs B [higher = worse]")
io.put('A: ' + disadvantagesA)
io.put('B: ' + disadvantagesB)
notGood = True
box7 = 0
box8 = 0
while notGood:
    box7 = io.getInt('A> ')
    box8 = 100 - box7
    io.put('So is it A: ', box7, ' and B: ', box8, '? [y/n]')
    if io.get('> ') == 'y':
        notGood = False
io.put('')
io.put("Rank advantages of A vs disadvantages of A")
io.put('Advantages: ' + advantagesA)
io.put('Disadvantages: ' + disadvantagesA)
notGood = True
box1 = 0
box2 = 0
while notGood:
    box1 = io.getInt('Advantage> ')
    box2 = 100 - box1
    io.put('So is it advantage: ', box1, ' and disadvantage: ', box2, '? [y/n]')
    if io.get('> ') == 'y':
        notGood = False
io.put('')
io.put("Rank advantages of B vs disadvantages of B")
io.put('Advantages: ' + advantagesB)
io.put('Disadvantages: ' + disadvantagesB)
notGood = True
box3 = 0
box4 = 0
while notGood:
    box3 = io.getInt('Advantage> ')
    box4 = 100 - box3
    io.put('So is it advantage: ', box3, ' and disadvantage: ', box4, '? [y/n]')
    if io.get('> ') == 'y':
        notGood = False
io.put('')
box9 = box5 + box1
box11 = box3 + box6
box10 = box2 + box7
box12 = box4 + box8
finalA = box9 - box10
finalB = box11 - box12
if finalA > 0 and finalB > 0:
    if finalA > finalB:
        io.put('Both choices are solid options but A is slightly better')
    else:
        io.put('Both choices are solid options but B is slightly better')
elif finalA < 0 and finalB < 0:
    io.put('Both options are negatives. This is shown to be a symptom of a depressed mindset.')
    if finalA > finalB:
        io.put('Option A is best though')
    elif finalA < finalB:
        io.put('Option B is best though')
    else:
        io.put('Both are tied.')
else:
    if finalA > finalB:
        io.put('Option A is best')
    elif finalA < finalB:
        io.put('Option B is best')
    else:
        io.put('Both are tied')
