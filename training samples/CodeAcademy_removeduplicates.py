'''
    Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

    For example: remove_duplicates([1,1,2,2]) should return [1,2].

    Don't remove every occurrence, since you need to keep a single occurrence of a number.
    The order in which you present your output does not matter. So returning [1,2,3] is the same as returning [3,1,2].
    Do not modify the list you take as input! Instead, return a new list.

'''

def remove_duplicates(LmD):             # Liste mit Duplikaten = LmD
    LoD = []
    print len(LmD)                            # liste ohne Duplikate = LoD

    if len(LmD) > 0 :
        LoD.append(LmD[0])    
        for doppelt in LmD :
            for unique in LoD :
                if doppelt == unique :
                    break
                elif doppelt != unique :
                    while LoD.index(unique) + 1 < len(LoD) :
                        break
                    else:
                        LoD.append(doppelt)
    print LoD
      
 
    
LmD = [1, 4, 3, 4, 5, 6, 4, 4, 1.098, 'a', 'c', 'a', 'd', 'a', 'Verlag', 'Hauptschule', 'Schule', 'Verlag', 'Schule']
# LmD = []
# LmD = ['Verlag']
# LmD = [1.098, 'Verlag']

remove_duplicates(LmD)