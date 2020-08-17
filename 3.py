def canCompleteCircuit(gas, cost):
    N = len(gas)
    idxs = []
    for i in range(N):
     if gas[i] >= cost[i]:
         j = i + 1
         tank = gas[i] - cost[i]
         while tank >= 0 and j < i + N:
             tank += gas[j % N] - cost[j % N]
             j += 1
             if tank >= 0:
                 idxs.append(i)
         return idxs
