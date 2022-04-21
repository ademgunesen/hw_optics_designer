class radiant:
    def __init__(self,x,y,p):
        self.x = x
        self.y = y
        self.p = p

    def get_obj(self):
        obj= []
        rad={
            "type": "radiant",
            "x": self.x,
            "y": self.y,
            "p": self.p
        }
        obj.append(rad)
        return obj

class black_line:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
  
    def get_obj(self):
        obj= []
        bline = {
            "type": "blackline",
            "p1": {
                "type": 1,
                "x": self.x1,
                "y": self.y1,
                "exist": "true"
            },
            "p2": {
                "type": 1,
                "x": self.x2,
                "y": self.y2,
                "exist": "true"
            }
        }
        obj.append(bline)
        return obj

class lens:
    def __init__(self,x,y,r,f):
        self.x = x
        self.y = y
        self.r = r
        self.f = f
        
    def get_obj(self):
        obj= []
        lens = {
            "type": "lens",
            "p1": {
                "type": 1,
                "x": self.x,
                "y": self.y-self.r,
                "exist": "true"
            },
            "p2": {
                "type": 1,
                "x": self.x,
                "y": self.y+self.r,
                "exist": "true"
            },
            "p": self.f
        }
        obj.append(lens)
        return obj

class ruler:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2    
        
    def get_obj(self):
        obj= []
        rul={
            "type": "ruler",
            "p1": {
                "type": 1,
                "x": self.x1,
                "y": self.y1,
                "exist": "true"
            },
            "p2": {
                "type": 1,
                "x": self.x2,
                "y": self.y2,
                "exist": "true"
            }
        }
        obj.append(rul)
        return obj