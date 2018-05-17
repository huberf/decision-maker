class Decider:
    def __init__(self):
        doNothing = True

    def final(self):
        finalA = weightA()
        finalB = weightB()
        toReturn = { 'choice': '', 'message': '' }
        if finalA > 0 and finalB > 0:
            if finalA > finalB:
                toReturn['choice'] = 'a'
                toReturn['message'] = 'Both are solid choices.'
            else:
                toReturn['choice'] = 'b'
                toReturn['message'] = 'Both are solid choices.'
        elif finalA < 0 and finalB < 0:
            if finalA > finalB:
                toReturn['choice'] = 'a'
            else:
                toReturn['choice'] = 'b'
        else:
            if finalA > finalB:
                toReturn['choice'] = 'a'
            elif finalA < finalB:
                toReturn['choice'] = 'b'
            else:
                toReturn['choice'] = None
                toReturn['message'] = 'Options are tied'
        return toReturn
