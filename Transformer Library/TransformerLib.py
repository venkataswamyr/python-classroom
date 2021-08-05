class TransformerLib:
    def __init__(self, *args):
        if len(args) == 0:
            self.f=0
            self.N=0
            self.Phi=0
            
            self.Pout=0
            self.Pfe=0
            self.Pcu=0
            
            self.E2=0
            self.V2=0
                  
        elif len(args) == 8:
            self.f=args[0]
            self.N=args[1]
            self.Phi=args[2]
            
            self.Pout=args[3]
            self.Pfe=args[4]
            self.Pcu=args[5]
            
            self.E2=args[6]
            self.V2=args[7]
            
        self.EMF=4.44*self.f*self.N*self.Phi
        
        if self.Pout+self.Pfe+self.Pcu ==0:
            self.Eff=0
        else:
            self.Eff=self.Pout/(self.Pout+self.Pfe+self.Pcu)*100
            
        if self.E2==0:
            self.Regulation=0
        else:
            self.Regulation=(self.E2-self.V2)/(self.E2)*100
        
    def TransformerEMF(self, *args):
        if len(args) == 3:
            self.f=args[0]
            self.N=args[1]
            self.Phi=args[2]
            self.EMF=4.44*self.f*self.N*self.Phi
        else:
            print('Pass only three parameters')
            
    def TransformerEfficiency(self, *args):
        if len(args) == 3:
            self.Pout=args[0]
            self.Pfe=args[1]
            self.Pcu=args[2]
            if self.Pout+self.Pfe+self.Pcu ==0:
                self.Eff=0
            else:
                self.Eff=self.Pout/(self.Pout+self.Pfe+self.Pcu)*100
        else:
            print('Pass only three parameters')   
    
    def TransformerRegulation(self, *args):
        if len(args) == 2:
            self.E2=args[0]
            self.V2=args[1]
            if self.E2==0:
                self.Regulation=0
            else:
                self.Regulation=(self.E2-self.V2)/(self.E2)*100
        else:
            print('Pass only two parameters')
        
        