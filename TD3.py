import unittest

class Tree:
    def __init__(self, symbol, *children):
        self.__symbol = symbol
        self.__children = children

    def label(self):
        return self.__symbol


    def children(self):
        return self.__children

    def nb_children(self):
        return len(self.__children)

    def child(self,i):
        return self.__children[i]

    def is_leaf(self):
        if len(self.__children)==0:
            return True
        else:
            return False

    def depth(self):
        m=[]
        if self.is_leaf()==True:
            return 0
        for i in range(0,len(self.__children)):
            m.append(self.__children[i].depth() +1)
        return max(m)

    def __str__(self):
        m=self.label()
        if self.is_leaf()==True:
            return m
        m=m+'('
        for i in range(0,len(self.children())-1):
            m=m+ str(self.child(i))+','
        return m+str(self.child(len(self.children())-1))+')'

    def __eq__(self, __value):
        if self.label()==__value.label():
            for i in range (0,len(self.children())):
                if self.child(i)!=__value.child(i):
                    return False
            return True
        return False

    def deriv(self, var):
        if self.is_leaf():
            if self.label() == var:
                return Tree('1')
            else:
                return Tree('0')
        if self.label() == '+':
            # dérivée d'une somme = somme des dérivées
            return Tree('+', *(child.deriv(var) for child in self.children()))
        if self.label() == '*':
            # Dérivée d'un produit = somme des dérivées partielles
            terms = []
            for i in range(len(self.children())):
                # dérivée partielle : dérivée du i-ème facteur * les autres non dérivés
                derived_i = self.child(i).deriv(var)
                others = [self.child(j) if j != i else derived_i for j in range(len(self.children()))]
                terms.append(Tree('*', *others))
            return Tree('+', *terms)
        # Autres opérateurs : retourne 0
        return Tree('0')


if __name__ == '__main__':
    t= Tree('+',
            Tree('+',
                 Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X'))),
                 Tree('*', Tree('5'), Tree('X'))),
            Tree('7'))
    print(t.deriv('X'))