#5.write class and function for the equation sqrt(x1-x2) ^ 2 + sqrt( y1 – y2 ) ^2 using try except handling.
class numbers:
    def __init__(self,a,b,c,d):
        self.x1=a
        self.x2=b
        self.y1=c
        self.y2=d
    def equation(self):
        import math
        try:
            x1=float(self.x1) 
            x2=float(self.x2)
            y1=float(self.y1) 
            y2=float(self.y2) 
            d=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
            return d
        except:
            print('Enter proper numeric values.')
            
