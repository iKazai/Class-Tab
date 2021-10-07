class Tab:
    def __init__(self, donnees=None):
        if donnees == None:
            self.contenant, self.id_fin, self.len_contenant = [None]*8, 0, 8
        else:
            self.contenant = [None]*len(donnees)*2
            for i in range(len(donnees)):
                self.contenant[i] = donnees[i]
            self.id_fin = i
            self.len_contenant = len(donnees)*2
        return None

    def ajout(self, a):
        if self.id_fin < self.len_contenant-1:
            self.id_fin += 1
            self.contenant[self.id_fin] = a
        else:
            newcontenant = [None]*self.len_contenant*2
            for i in range(len(self.contenant)):
                newcontenant[i] = self.contenant[i]
            self.contenant = newcontenant
            self.id_fin += 1
            self.len_contenant = self.len_contenant*2
            self.contenant[self.id_fin] = a
        return None
    
    def __str__(self):
        string = ''
        for elem in self.contenant:
            if elem != None:
                string += str(elem) + ', '
        return string
    
    def __len__(self):
        length = 0
        for elem in self.contenant:
            if elem != None:
                length += 1
        return length
    
    def __getitem__(self,n):
        return self.contenant[n]
    
    def __setitem__(self,n,val):
        self.contenant[n] = val
        return None