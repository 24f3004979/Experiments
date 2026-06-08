'''
PS: Find substring count from given string
traversal from left to right
'''

def count_substring(string, sub_string):
    
    '''
    Making all possible pairs out of the string
    eliminating all non length equivalent strings
    comparing final chunk sets
    
    # First approach
        Split the string with 3 elements window then trace count
        Failed with : Not just straight 3 window can capture the essense
    # Second brute force
        Making all possible pairs
        scanning with just sub string length
        counting final
        
        Wrong Intuitivly
            Since we are taking account of just the streaming elements
            Not into the whole string element :)
        
    # Third Approach
        Making window attempt with shifting first pointer to the next
        
    CORRECT APPROACH :)
    '''
    count = 0
    l = 0
    r = len(sub_string)
    
    # traversal with shiftiing with each iteration
    while r <= len(string):
        el = string[l:r]
        if el == sub_string:
            count += 1
            
        # Shifting for next element
        l += 1
        r += 1
    return count
    
    
    
    
    
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
