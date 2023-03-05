def mergeArrays(self,a,b,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    '''
    i = j = 0
    union = []
    while i < n and j < m:
        if a[i] <= b[j]:
            if len(union) == 0 or a[i] != union[-1]:
                union.append(a[i])
            i += 1
        else:
            if len(union) == 0 or b[j] != union[-1]:
                union.append(b[j])
            j += 1
    while i < n:
        if a[i] != union[-1]:
            union.append(a[i])
        i += 1
    
    while j < m:
        if b[j] != union[-1]:
            union.append(b[j])
        j += 1
    return union