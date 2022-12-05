class A:
    def func(self):
        print("I'm in A")                          
class B(A):
    def func(self):
        print("I'm in B")                             
obj=B()
obj.func()