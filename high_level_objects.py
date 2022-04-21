from primitives import *

class h_lvl_obj:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.obj = []
    def build(self):
        print("not defined")
    def get_obj(self):
        self.build()
        o_list = []
        for i in self.obj:
            o_list += i.get_obj()
        return o_list
 
class retina(h_lvl_obj):

    def __init__(self,x,y,size,d,p=0.5):
        self.x = x
        self.y = y
        self.size = size
        self.d = d
        self.p = p
        self.obj = []
        
    def build(self):
        self.obj = []
        for i in range ((self.y-self.size//2),(self.y+self.size//2+self.d),self.d):
            self.obj.append(radiant(self.x,i,self.p))

class eye(h_lvl_obj):
    
    def __init__(self,x,y,pup):
        self.x = x
        self.y = y
        self.pup = pup
        self.obj = []
    
    def build(self):    
        x=self.x
        y=self.y
        pup=self.pup
        self.obj = []
        self.obj.append(black_line(x-20, y+100,x-20, y-100))
        self.obj.append(black_line(x-20, y+100,x+100,y+100))
        self.obj.append(black_line(x-20, y-100,x+100,y-100))
        self.obj.append(black_line(x+160,y+80, x+100,y+100))
        self.obj.append(black_line(x+160,y-80, x+100,y-100))
        self.obj.append(black_line(x+180,y+60, x+160,y+80))
        self.obj.append(black_line(x+180,y-60, x+160,y-80))
        self.obj.append(black_line(x+200,y+pup/2, x+180,y+60))
        self.obj.append(black_line(x+200,y-pup/2, x+180,y-60))
        self.obj.append(lens(x+200,y,pup/2,200))
        self.obj.append(radiant(x+200,y+pup/2, 0))
        self.obj.append(radiant(x+200,y-pup/2, 0))
        self.obj.append(retina(x,y,200-20,20))

class cam(h_lvl_obj):  
    def __init__(self,x,y,m12_lens = "default"):
        self.x = x
        self.y = y
        self.m12_lens = m12_lens
        self.obj = []
        
    def build(self):
        x=self.x
        y=self.y
        self.obj = []
        if self.m12_lens == "default":
            self.obj.append(m12_lens(x-300,y,60,160))
            print("default lens")
        else:
            self.obj.append(self.m12_lens)
            print("custom_lens")
        self.obj.append(black_line(x+0,  y-120,x-100,y-120))
        self.obj.append(black_line(x+0,  y+120,x-100,y+120))
        self.obj.append(black_line(x-100, y-60,x-100,y-120))
        self.obj.append(black_line(x-100, y+60,x-100,y+120))
        self.obj.append(black_line(x+0,  y-200,x+0,  y+200))
        self.obj.append(black_line(x+20, y-200,x+20, y+200))
        self.obj.append(black_line(x+0,  y+200,x+20, y+200))
        self.obj.append(black_line(x+0,  y-200,x+20, y-200))
    
    def set_lens(self,m12_lens):
        self.m12_lens = m12_lens

class ring_light(h_lvl_obj):
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.obj = []
        
    def build(self):
        self.obj = []
        self.obj.append(radiant(self.x,self.y-self.r, 0))
        self.obj.append(radiant(self.x,self.y+self.r, 0))

class m12_lens(h_lvl_obj):
    def __init__(self,x,y,f):
        self.x = x
        self.y = y
        self.f = f
        self.obj = []

    def build(self):
        x=self.x
        y=self.y
        f=self.f
        self.obj = []
        self.obj.append(black_line(x, y-60,x,y-80))
        self.obj.append(black_line(x, y+60,x,y+80))
        self.obj.append(black_line(x+60, y-80,x,y-80))
        self.obj.append(black_line(x+60, y+80,x,y+80))
        self.obj.append(black_line(x+60, y+60,x+200,y+60))
        self.obj.append(black_line(x+60, y-60,x+200,y-60))
        self.obj.append(black_line(x+60, y+40,x+60,y+80))
        self.obj.append(black_line(x+60, y-40,x+60,y-80))
        self.obj.append(lens(x,y,60,f))