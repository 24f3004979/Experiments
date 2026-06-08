'''
    Traversal with str2
        finding differnce
            if not found
                remove the last element from str1
            scan for final index listing
    '''
    m = len(str2)
    diff = ''
    repeating_element = []
    diff_found = False
    for i in range(0,m):
        e1 = str1[i]  # target to search with
        e2 = str2[i]
        if e2 != e1:
            diff = e1  # found difference
            diff_found = True
            break
        elif (e2 == e1)and(e2 in e1[:i]):
            diff = e1
            diff_found = True
    
    # Final Scan for indexing differences
    indexes = []
    
    for e in range(0, len(str2)):
        elem = str1[e]
        if elem == diff:
            # check for equality before adding into the main array
            potential_modified = str1[:e] + str1[e+1:]
            if potential_modified == str2:
                indexes.append(e) # given index
    # last element check
    last_index = len(str1)
    last_elem = str1[last_index-1]
    
    if last_elem == diff:
        
        potential_modified = str1[:-1]
        if potential_modified == str2:
            indexes.append(last_index - 1) # given index
            
    if not diff_found:
        if len(indexes) == 0:
            return [-1]
                
    return indexes
