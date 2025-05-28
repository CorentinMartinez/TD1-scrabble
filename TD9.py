class Polyq:
    def __init__(self,coeff,n,q):
        self.n=n
        self.q=q
        self.coeff=[c%q for c in coeff]
        if len(self.coeffs) < n:
            self.coeff += [0] * (n - len(self.coeff))
        else:
            self.coeff = self.coeff[:n]

    def __add__(self,other):
        assert self.q==other.q
        assert self.n==other.n
        coeff=[(a+b)%c for a,b in zip(self.coeff,other.coeff)]
        return Polyq(coeff,n,q)

    def mul(self,other):
        assert self.q==other.q
        assert self.n==other.n
        coeff=[0]*self.n
        for i in range (0,len(self1.l)):
            for j in range(0,len(self.l2)):
                if i+j<n:
                    coeff[i+j]=(coeff[i+j]+coef[i]*coeff[j])%q
                else:
                    coeff[i+j-n]=(coeff[i+j-n]-coef[i]*coeff[j])%q
        return Polyq(coeff,n,q)

    def rescale(self,r):
        coeff=[c%r for c in self.coeff]
        return Polyq(coeff,n,q)

    def scalar(self,c):
        coeff=[(c*a)%q for a in self.coeff]
        return Polyq(coeff,n,q)