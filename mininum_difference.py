def solution(numbers, separation):
    '''req: 
        - fn takes arr of pos ints and a pos number, separation
        - find min abs diff bwt elements w/ indices that are at least separation apart
        
        >>> numbers = [1,5,4,10,9], separation = 3
        4
    '''
    # initialize min_diff var to infinity
    # iterate through numbers
    # calculate abs diff between elems
    # update min_diff if new one is found
    # return min_diff
    
    min_diff = float('inf')
    n = len(numbers)
    
    for i in range(n):
        for j in range(i + separation, n):
            difference = abs(numbers[i] - numbers[j])
            min_diff = min(min_diff, difference)
            
    return min_diff
