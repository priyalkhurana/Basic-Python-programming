#Write a program to accept type of figure square, 
# triangle and rectangle and fetch the values of the dimensions from the user
#  using parent class and calculate the area by using respective child classes. 
class values:
    def __init__(self,figure):
        self.figure=figure
    def dim_t(self,b,h):
        self.b=b
        self.h=h
    def dim_r(self,leng,br):
        self.leng=leng
        self.br=br
class cal_tr(values):
    def calc(self):
        print("AREA=%d",0.5*self.b*self.h)
class cal_Rec(values):
    def calc(self):
        print("AREA=%d",self.leng*self.br)
print("enter the figure:")
x=input()
A=values(x)
if(x=='triangle'):
    print("enter dimensions")
    x=int(input())
    y=int(input())
    A.dim_t(x,y)
    a1=cal_tr('triangle')
    a1.calc()
elif(x=='rectangle'):
    print("enter dimensions")
    x=int(input())
    y=int(input())
    A.dim_r(x,y)
    a2=cal_Rec('rectangle')
    a2.calc()
else:
    print("WRONG CHOICE!!!!")