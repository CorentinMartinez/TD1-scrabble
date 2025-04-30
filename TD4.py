def hnaif(key):
    valeur=0
    for i in key:
        valeur = valeur + ord(i)
    return valeur

def hjenkins(key):
    hash=0
    for i in key:
        hash+= ord(i)
        hash += hash << 10
        hash ^= hash >> 6
    hash += hash << 3
    hash ^= hash >> 11
    hash += hash << 15
    return hash

class hashtable:
    def __init__(self,h,length):
        self.__h = h
        self.__length=length
        self.__l=[None]*length
        self.__nb=0

    def put(self,key,value):
        loc=self.__h(key)%self.__length
        if self.__l[loc]==None:
            self.__l[loc]=[(key,value)]
        else:
            for i in range(0,len(self.__l[loc])):
                if self.__l[loc][i][0]==key:
                    self.__l[loc][i]=(key,value)
                    return
            self.__l[loc].append((key,value))
            slef.__nb+=1
            if self.__nb==self.__length:
                resize(self)

    def get(self,key):
        loc=self.__h(key)%self.__length
        if self.__l[loc]==None:
            return None
        else:
            for i in (0,len(self.__l[loc])):
                if self.__l[loc][i][0]==key:
                    return self.__l[loc][i][1]

    def repartition(self):
        import matplotlib.pyplot as plt
        y = []
        for i in range(0,self.__length):
            if self.__l[i]==None:
                y.append(0)
            else:
                y.append(len(self.__l[i]))
        N = len(y)
        x = range(N)
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()

    def resize(self):
        liste=[None]*2*self.__length
        #refaire une fonction put



if __name__ == '__main__':
    h=hashtable(hjenkins,320)
    f = open('frenchssaccent.dic','r')
    liste=[]
    for ligne in f:
        liste.append(ligne[0:len(ligne)-1])
    f.close()
    for key in liste:
        h.put(key,len(key))
    h.repartition()