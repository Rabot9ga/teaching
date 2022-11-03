import math

def find_max_triple(c):
    list_triang=[]
    for i in range(2, int(c**(1/2))+1):
        for j in range(i):
            if math.gcd(i, j)==1 and (i-j)%2!=0 and i**2+j**2<=c and sorted([i**2-j**2, 2*i*j, i**2+j**2]) not in list_triang:
                list_triang.append(sorted([i**2-j**2, 2*i*j, i**2+j**2]))
    return [{'number triples below-eq '+str(c): len(list_triang)}, {'max perimeter': sum(max(list_triang, key=sum))}, {'largest triple': [tuple(max(list_triang, key=sum))]}]