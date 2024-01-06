def matchingStrings(strings, queries):
    '''requirements: 
      - fn takes 2 arrs of strs
      - return freq of each query string that shows up in strings in an arr
    '''
    occurences = {}
    
    for string in strings:
        occurences[string] = occurences.get(string, 0) + 1
    
    freqs = [occurences.get(query, 0) for query in queries]
    
    return freqs

# make dict for occurence of str
# iterate through strings
# update count in dict
# use list comprehension to create arr of freqs

