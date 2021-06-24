sigma = ['#']
finals = []
states  = []
delta = {}
againInput = 'Invalid input. Try again.'


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

inputString= input('Enter the string you want to process: ')
inputString= (10*'#')+inputString+(10*'#')
inputString = list(inputString)
print(inputString)
index= 10


#This creates a new dictionary for each state to accomodate each transition for a given input
for s in states:
    delta[s] = {}
    for sig in sigma:
        delta[s][sig]=[None, None ,None]

print('Now choose the transition between each state and respective input')
for s in states: #loop for setting the transition between each state and input
    for sig in sigma:
        while True:
            nextState =input('in state \"' +s +'\" and when reading the value \"'+ sig +'\" type the desired next state. If you do not want to accomodate the transition leave this blank and press enter: ')
            if nextState in states:
                delta[s][sig][0]=nextState
            elif nextState=='':
                break
            else:
                print(againInput)
                continue
            write =input('Enter the value you would like to write on the tape:')
            if write in sigma:
                delta[s][sig][1]=write
            else:
                print(againInput)
                continue
            direction =input('Enter l for left transition and r for right:')
            if direction=='l' or 'r':
                delta[s][sig][2]=direction
                break
            else:
                print(againInput)
                continue
curState= states[0]
res=0
while True:
    if curState in finals:
        print('Accepted')
        break
    elif res == len(sigma):
        print('Rejected')
        break
    res = 0
    for s in sigma:
        if (not delta[curState][s][0]==None) and (s == inputString[index]):
            inputString[index]= delta[curState][s][1]
            if delta[curState][s][2]=='l':
                index= index-1
            else:
                index= index+1
            curState= delta[curState][s][0]
            print(inputString)
            print('Current State: 'curState)
        else:
            res = res+1
        
