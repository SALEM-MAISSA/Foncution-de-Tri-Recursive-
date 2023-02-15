
def tri_insertion(L):
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] > cle:
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle
                      

import random
liste = []
for k in range(10):
    liste.append(random.randint(0,20))
tri_insertion(liste)
                      

def tri_insertion(liste):
    L = list(liste) # copie de la liste
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] > cle:
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle
    return L
    
liste = []
for k in range(10):
    liste.append(random.randint(0,20))
liste_triee = tri_insertion(liste)

                      

def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1<n1 and i2<n2:
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    while i1<n1:
    	L12[i] = L1[i1]
    	i1 += 1
    	i += 1
    while i2<n2:
    	L12[i] = L2[i2]
    	i2 += 1
    	i += 1 
    return L12
                

L = fusion([1,6,10],[0,7,8,9])
                

def tri_fusion_recursif(L):
    n = len(L)
    if n > 1:
        p = int(n/2)
        L1 = L[0:p]
        L2 = L[p:n]
        tri_fusion_recursif(L1)
        tri_fusion_recursif(L2)
        L[:] = fusion(L1,L2)
    
def tri_fusion(L):
    M = list(L)
    tri_fusion_recursif(M)
    return M
                  

liste = []
for k in range(11):
    liste.append(random.randint(0,20))
liste_triee = tri_fusion(liste)
                  

import time
import numpy
                   
def rapport_temps(N):
    n = 100
    t1 = time.time()
    for k in range(n):
        liste = numpy.random.randint(0,N,size=N)
        tri_insertion(liste)
    t1 = time.time()-t1
    t2 = time.time()
    for k in range(n):
        liste = numpy.random.randint(0,N,size=N)
        tri_fusion(liste)
    t2 = time.time()-t2
    return t2/t1 
                   

def partition(L):
    n = len(L)
    pivot = L[n-1]
    i = 0
    j = 0
    while j < n-1:
        if L[j] <= pivot:
            L[i],L[j] = L[j],L[i]
            i += 1
        j += 1
    L[n-1],L[i] = L[i],L[n-1]
                

liste = []
for k in range(11):
    liste.append(random.randint(0,40)) 
                
partition(liste)

def partition(L,debut,fin):
    pivot = L[fin]
    i = debut
    j = debut
    while j < fin:
        if L[j] <= pivot:
            L[i],L[j] = L[j],L[i]
            i += 1
        j += 1
    L[fin],L[i] = L[i],L[fin]
    return i
                   

def tri_partition_recursif(L,debut,fin):
    if debut < fin:
        i = partition(L,debut,fin)
        tri_partition_recursif(L,debut,i-1)
        tri_partition_recursif(L,i+1,fin)
                   

def tri_partition(liste):
    L = list(liste)
    tri_partition_recursif(L,0,len(L)-1)
    return L
                   

liste = []
for k in range(11):
    liste.append(random.randint(0,40))
liste_triee = tri_partition(liste)
                   
        
def rapport_temps(N):
    n = 100
    t1 = time.time()
    for k in range(n):
        liste = numpy.random.randint(0,N,size=N)
        tri_fusion(liste)
    t1 = time.time()-t1
    t2 = time.time()
    for k in range(n):
        liste = numpy.random.randint(0,N,size=N)
        tri_partition(liste)
    t2 = time.time()-t2
    return t2/t1 
                   
