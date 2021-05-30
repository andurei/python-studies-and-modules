

def minDict(dictionary):
    min_price = min(zip(dictionary.values(), dictionary.keys()))
    return min_price 
    
def maxDict(dictionary):
    max_price = max(zip(dictionary.values(), dictionary.keys()))
    return max_price 

def commonKeys(dict1, dict2): # chaves em comum em dois dicionários
    return dict1.keys() & dict2.keys()

def intersectionKeys(dict1, dict2): # chaves no dicionário1 que não têm no dicionário2
    return dict1.keys() - dict2.keys()

def commonKeyValue(dict1, dict2): # (chaves e valores) em comum em dois dicionários
    return dict1.items() & dict2.items()
