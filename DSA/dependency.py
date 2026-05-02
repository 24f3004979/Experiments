def max_sem(sems):
    completed = set()
    
    # computing length of all less then one into one

    for s in sems.keys():

        if len(sems[s]) < 1:
            completed.add(sems[s])

        # deleting dependency listing
        for i in sems[s]:
            if not(_ in completed):
                e.append(_)
                


sems = {0:[],1:[],2:[],3:[],4:[0],5:[0,2],6:[1,3],7:[2],8:[0,4,6],9:[5,7],10:[6],11:
[3,7],12:[8,9],13:[9,10,11]}
