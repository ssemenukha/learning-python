def clean_list(inlist):
    outlist = []
    for item in inlist:
        isinlist = False
        for ol in outlist:
            if (item == ol) and (type(item) == type(ol)):
                isinlist = True
                break
            
        if not isinlist:
            outlist.append(item)
    return outlist

ret = clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])
print ret