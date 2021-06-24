sigma = []
finals = []
states  = []
delta = {}
partitions = {}
parCount = 3
againInput = 'Invalid input. Try again.'

'''
def stateExists(s):
    if s in states or s in 
    for x in states:
        if s == x:
            return True
            break
    for x in sigma:
        if s == x:
            return True
            break
'''
def procInput(mainArray, name):
    print('Enter an element of '+ name +' then press "Enter" for the next element. Press (n) then "Enter" to finish.')
    while True:
        userIn = input()
        if userIn == 'n':
            break
        elif (userIn in mainArray) or ((mainArray is finals) and (userIn not in states)) or not userIn.strip():
            print(againInput)
        else:
            mainArray.append(userIn)

#Take user input for the alphabet (Sigma)
procInput(sigma, 'Sigma (Inputs)')

#Take user input for states (Q)
procInput(states, 'Q (States)')

#Take user input for final state(s) (F)
procInput(finals, 'final states set')

#This creates a new dictionary for each state to accomodate each transition for a given input
for s in states:
    delta[s] = {}
    if s in finals:
        delta[s]['Par']=2
    else:
        delta[s]['Par']=1
    
    for sig in sigma:
        delta[s][sig]=''
        

print('Now choose the transition between each state and respective input')
for s in states: #loop for setting the transition between each state and input
    for sig in sigma:
        while True:
            nextState =input('For state \"' +s +'\" and input \"'+ sig +'\" type the desired next state(transition): ')
            if nextState in states:
                delta[s][sig]=nextState
                break
            else:
                print(againInput)



print('This is the current transition table (before minimization):\n', delta)
print('These are the alphabet:\n', sigma)
print('These are the state(s):\n', states)
print('These are the final state(s):\n', finals)
#Set partitioning starts here
delta2 = delta
for d2 in delta2:
    parCount= parCount + 1
    
    for d in delta:
        delta2 = delta
        equal = True
        if delta[d]['Par']==delta2[d2]['Par'] and d!=d2:
            for inp in sigma:
                nextState1 = delta[d][inp]
                nextState2=  delta2[d2][inp]
                nextPar1= delta[nextState1]['Par']
                nextPar2=  delta2[nextState2]['Par']
                if nextPar1 != nextPar2:
                    equal = False
            if equal:
                delta[d]['Par']=parCount
                delta[d2]['Par']= parCount
parCount= parCount + 1
for d in delta:
    if delta[d]['Par']< 3:
        delta[d]['Par']= parCount
        parCount= parCount + 1
    
print('This is the current transition table (after minimization):\n', delta)
        
