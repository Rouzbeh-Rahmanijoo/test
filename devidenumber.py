
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

def devidenumber(a):
    list_1 = list(a.strip(" "))
    b = []
    for a in list_1:
      if a.isnumeric():
        b.append(a)

    return listToString(b)