def find_zigzag_triples(numbers):
    '''req:
        - fn takes arr of int
        - return arr of 1s and 0s; 1 --> zigzag
        
        >>> [1,2,1,3,4]
        [1,1,0]
    '''
    # sliding window approach
    zigzag_triples = []
    n = len(numbers)
  
    for i in range(n - 2):
        window = numbers[i:i + 3]  # Sliding window of size 3
        if window[0] < window[1] > window[2] or window[0] > window[1] < window[2]:
            zigzag_triples.append(1)
        else:
            zigzag_triples.append(0)
    return zigzag_triples

#2nd solution w/o sliding window

def solution(numbers):
    '''req:
        - fn takes arr of int
        - return arr of 1s and 0s; 1 --> zigzag
        
        >>> [1,2,1,3,4]
        [1,1,0]
    '''
    zigzag_triplets = []
    n = len(numbers)
    
    for i in range(n - 2):
        if is_zigzag(numbers[i], numbers[i + 1], numbers[i + 2]):
            zigzag_triplets.append(1)
        else:
            zigzag_triplets.append(0)
            
    return zigzag_triplets
        
def is_zigzag(a, b, c):
    '''checks if 3 elems are a zigzag'''
    return (a > b < c) or (a < b > c)  
