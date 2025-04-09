## Exo 1

class Polynomial:
    def __init__(self,l):
        self.l=l

    def __str__(self):
        term=[]
        polynome=""
        if len(self.l)==2:
            if self.l[1]==1:
                polynome+=""+f"X"
            if self.l[1]!=1 and self.l[1]!=0:
                if self.l[1]>0:
                    polynome+=""+f"{self.l[1]}*X"
                else:
                    if self.l[1]==-1:
                        polynome+="-"+f"X"
                    else:
                        polynome+=""+f"{self.l[1]}*X"
            if self.l[0]>0:
                polynome+="+"+f"{self.l[0]}"
            if self.l[0]<0:
                polynome+="-"+f"{self.l[0]}"
        else:
            for i in range (len(self.l)-1,-1,-1):
                if i==0:
                    if self.l[i]!=0:
                        polynome+="+"+f"{self.l[i]}"
                elif i==1:
                    if self.l[i]==1 or self.l[i]==-1:
                        if self.l[i]==1:
                            polynome+="+"+f"X"
                        else:
                            polynome+="-"+f"X"
                    elif self.l[i]!=0:
                        if self.l[i]<0:
                            polynome+="+"+f"{self.l[i]}*X"
                elif i==len(self.l)-1:
                    if self.l[i]==1 or self.l[i]==-1:
                        if self.l[i]==1:
                            polynome+=""+f"X**{i}"
                        else:
                            polynome+="-"+f"X**{i}"
                    elif self.l[i]!=0:
                        polynome+=""+f"{self.l[i]}*X**{i}"
                else:
                    if self.l[i]==1 or self.l[i]:
                        if self.l[i]==1:
                            polynome+="+"+f"X**{i}"
                        else:
                            polynome+="-"+f"X**{i}"
                    elif self.l[i]!=0:
                        if self.l[i]>0:
                            polynome+="+"+f"{self.l[i]}*X**{i}"
                        else:
                            polynome+=""+f"{self.l[i]}*X**{i}"
        return polynome

    def __add__(self,self2):
        somme=[]
        if len(self.l)>len(self.l):
            somme=self.l[len(self.l)-1]
            for k in range(0,len(self.l)-len(self2.l)+1):
                somme+="+"+self.l[len(self.l)-k]
        if len(self2.l)>len(self.l):
            somme=self.l[len(self2.l)-1]
            for k in range(0,len(self2.l)-len(self.l)+1):
                somme+="+"+self.l[len(self.l)-k]
        for k in range(1,min(len(self.l),len(self2.l))):
            if self.l[min(len(self2.l),len(self.l))-k]!=0:
                somme+="+"+self.l[min(len(self2.l),len(self.l))-k]
            if self2.l[min(len(self2.l),len(self.l))-k]:
                somme+="+"+self2.l[min(len(self2.l),len(self.l))-k]
        return somme

if __name__ == '__main__':
        p= Polynomial([1,-1,-1,-1,1])
        print(str(p))

## Exercice 2+3+4+5

class Polyq:
    def __init__(self,coef,q,n):
        self.q=q
        self.n=n
        self.coef=coef[:]
        for k in range(len(coef)):
            for j in range(1,int(((len(coef)-1)-k)/n)+1):
                coef[k]+=((-1)**(j))*coef[k+j*n]
        for j in range(n,len(coef)):
            coef[j]=0
        self.coef = [c%q for c in coef]


    def __str__(self):
        if self.coef[0]!=0:
            m=str(self.coef[0])+signe(self.coef[1])
        else:
            m=signe(self.coef[1])
        for i in range(1,len(self.coef)-1):
            if self.coef[i]==0:
                continue
            else:
                m+=str(abs(self.coef[i]))+'*X^'+str(i)+signe(self.coef[i+1])
        return m+str(self.coef[len(self.coef)-1])+'*X^'+str(len(self.coef)-1)


    def signe(x):
        if x<0:
            return "-"
        else:
            return "+"


    def scalar(c,P):
        for i in range(len(P.coef)):
            P.coef[i]=c*P.coef[i]
        return P

    def rescale(self,r):
        Q=self.coef
        for i in range(len(Q)):
            Q[i]=Q[i]%r
        return Polyq(Q)

    def __add__(self,P2):
        Q=[0]*(min(len(self.coef),len(P2.coef)))
        for i in range(min(len(self.coef),len(P2.coef))):
            Q[i]=self.coef[i]+P2.coef[i]
        if len(self.coef)>=len(P2.coef):
            return Polyq(Q+self.coef[(len(self.coef)-len(P2.coef))+1:],self.q,self.n)
        elif len(self.coef)<=len(P2.coef):
            return Polyq(Q+P2.coef[(len(P2.coef)-len(self.coef))+1:],self.q,self.n)
        else:
            return Polyq(Q,self.q,self.n)


    def __mul__(self,P):
        Q=[0]*len(self.coef)
        for i in range(len(self.coef)):
            for k in range(i):
                Q[i]+=self.coef[k]*self.coef[i-k]
        return Polyq(Q,self.n,self.q)
