def patternvector(H):
    P=np.zeros(len(H))
    for i,val in enumerate(H):
        if val != 0:
            P[i]=1
    return P

def Patternagreement(P):
    if max(P)>1:
        raise ValueError("Somethings wrong here")
    K= len(P)
    TDU=0
    TU=0
    for i in range(K-2):
        for j in range(i+1,K-1):
            for m in range(j+1,K):
                if P[i] == 1 and P[j] == 0 and P[m] == 1:
                    TDU += 1 # 101 pattern, bimodal (TDU)
                if P[i] == 1 and P[j] == 1 and P[m] == 0:
                    TU += 1   # 110 pattern, unimodal (TU)
                if P[i] == 0 and P[j] == 1 and P[m] == 1:
                    TU += 1   # 011 pattern, unimodal (TU)      
    if TU == 0 and TDU == 0: #U=1
        S = sum(P)
        A= 1-(S-1)/(K-1) 
    elif ((K-2)*(TU+TDU))==0:
        A = 0
    else:
        U = ((K-2)*TU-(K-1)*TDU)/((K-2)*(TU+TDU)) # normal case: U as in equation (2) on p.332      	
        S = sum(P)                        # number of non-empty
        A = U*(1-(S-1)/(K-1))             # calculating agreement A
        if K==1:
            A = 0            # lack of agreement, defined as 0
        if sum(P) == 1:
            A = 1          # only one value, defined as 1
    return A        


def agreement(V):
    if len(V)<3:
        raise ValueError("Arrays must have the size 3 or bigger")
    elif min(V)<0:
        raise ValueError( "error")
    else:
        AA=0
        #A=[]
        k=len(V)
        N=sum(V)
        R=V
        for i in range(k):
            P=patternvector(R)
            if max(P)==0:
                break
            A=Patternagreement(P)
            #print(R)
            m = np.ma.masked_equal(R, 0.0, copy=False).min()
            L=P*m
            w=sum(L)/N
            AA+= w*A
            R= R-L
    return AA
            
