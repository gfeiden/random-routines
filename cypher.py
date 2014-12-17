#
#
class simpleCypher():
    """ simple cypher for astro division assmebly emails """ 

    def __init__(self):
        self.alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
        self.num = len(self.alpha)
        
    def encodeSimplePolyAlpha(self, s):
        """ encode a message """
        import numpy.random as rand
    
        rand.seed()
        seed = int(rand.random()*24.)
        key = self.alpha[seed]
        
        n = 1
        s = s.upper()
        ns = ''
        for l in s:
            try:
                opos = self.alpha.index(l)
                move = int((-1.0)**n * seed)
                npos = opos + move
                if npos > (self.num - 1):
                    npos = npos - self.num
                elif npos < 0:
                    npos = self.num + npos
                else:
                    pass
                nl = self.alpha[npos]
            except:
                nl = l
            ns = '{0}{1}'.format(ns, nl)
            n += 1
        return '{0}{1}'.format(key, ns)
        
    def decodeSimplePolyAlpha(self, s):
        """ decode a message """
        s = s.upper()
        key = self.alpha.index(s[0])
        
        n = 0
        ns = ''
        for l in s[1:]:
            try:
                opos = self.alpha.index(l)
                move = int((-1.0)**n * key)
                npos = opos + move
                if npos > (self.num - 1):
                    npos = npos - self.num
                elif npos < 0:
                    npos = self.num + npos
                else:
                    pass
                nl = self.alpha[npos]
            except:
                nl = l
            ns = '{0}{1}'.format(ns, nl)
            n += 1
        return ns
