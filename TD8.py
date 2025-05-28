import struct

f=open("the_wall.wav","rb")
data=f.read()
print(struct.unpack_from("I",data,offset=16),struct.unpack_from("H",data,offset=22),struct.unpack_from("I",data,offset=40))
d=struct.unpack_from("I",data,offset=40)[0]//4

def exo1():
    print(d)
    L=[]
    s=44
    for i in range(0,d):
        L.append(struct.unpack_from("hh",data,s))
        s=s+4 #le 4 vient de la longueur de chaque ligne (32/8=4)
    print(L[0])
    return L

def exo2(L,nomfichier):
    Thewall=open(nomfichier,"wb")
    taillefichier=len(L)+44-8
    #on construit le header à la main
    Thewall.write(data[0:4])
    Thewall.write(struct.pack("I",taillefichier))
    Thewall.write(data[8:40])
    Thewall.write(struct.pack("I",len(L)*4))
    for i in range(0,len(L)):
        #on convertit en bytes les éléments de notre liste 2 à 2
        Thewall.write(struct.pack("h",L[i][0]))
        Thewall.write(struct.pack("h",L[i][1]))
    Thewall.close()

def exo3(L,nomfichier):
    out=[]
    for i in range(0,len(L)//2-1):
        out.append(L[2*i+1]) #on construit une liste annexe où on garde que une sample sur 2
    return exo2(out,nomfichier)

