#flatten(lst)        Flattens the list 
                    #ie input = [1,2,3, [1,2,3,[3,4],2]]
                    #output = [1,2,3,1,2,3,3,4,2]"""
                                      
def flatten(lst):
    l=[]
    for i in lst:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, list):
                    for k in j:
                        l.append(k)
                else:
                    l.append(j)
        else:
            l.append(i)
    return l
    
print(flatten([1,2,3, [1,2,3,[3,4],2]]))
