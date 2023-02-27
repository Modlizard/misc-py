visited = []
queue = []
#1200,570,705,075,525,750,1020,255,1002,372,345,840,804,174,165
#51
#xy,yz,zx,yz,xy,yz,zx,yz,xy,yz,zx
initState = [12,0,0]
goalState = [6,6,0]

def pour(a,b,inState):
    state = inState.copy()
    if state[a] == 0 or (b == 1 and state[1] == 7) or (b == 2 and state[2] == 5):
        return state
    else:
        cap = {0:12,1:7,2:5}
        bTotal = min(state[a] + state[b], cap[b])
        change = bTotal-state[b]
        state[a] -= change
        state[b] += change
        return state

def expand(state):
    visited.append(state)
    for a,b in [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]:
        nextState = pour(a,b,state)
        # print('a', state)
        # print('b', nextState)
        if not(nextState in visited):
            queue.append(nextState)
    while len(queue) > 0:
        testState = queue.pop(0)
        if testState == goalState:
            print("Solution found")
            break
        print(testState)
        expand(testState)

expand(initState)