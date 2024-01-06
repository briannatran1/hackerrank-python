def lonelyinteger(a):
    ''' requirements:
        - fn given arr of ints that are dupes except 1 elem
        - return unique int
    '''
    freqs = {}
    
    for num in a: 
        freqs[num] = freqs.get(num, 0) + 1
        
    for key, value in freqs.items():
        if value == 1:
            return key    
    
# create dict 
# iterate through arr and update dict
# check for key value that is 1 and return key 
