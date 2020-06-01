class DCGenerator:
    def __init__(self, *args):
        if len(args) == 0:
            self.Phi=0
            self.Z=0
            self.N=0
            self.WType='lap'
            self.P=0
            self.A=0
            self.E=0
        elif len(args) >= 5:
            self.Phi=args[0]
            self.Z=args[1]
            self.N=args[2]
            self.WType=args[3]
            if self.WType == 'lap':
                self.P=args[4]
                self.A=args[5]
            elif self.WType == 'wave':
                self.P=args[4]
                self.A=2
            self.E=(self.Phi*self.Z*self.N*self.P)/(60.0*self.A)
        
    def report(self):
        print('Phi=',self.Phi,'Wb')
        print('Z=',self.Z)
        print('N=',self.N)
        print('WType is',self.WType)
        print('P=',self.P)
        print('A=',self.A)
        print('EMF=',self.E,'Volts')
    
    def emf(self, *args):
        self.Phi=args[0]
        self.Z=args[1]
        self.N=args[2]
        self.WType=args[3]
        if self.WType == 'lap':
            self.P=args[4]
            self.A=args[4]
        elif self.WType == 'wave':
            self.P=args[4]
            self.A=2
        self.E=(self.Phi*self.Z*self.N*self.P)/(60.0*self.A)
        
        