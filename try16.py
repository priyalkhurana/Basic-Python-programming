class reportcard:
    a=[0,0,0,0,0]
    res=0
    def inputd(self):
        for i in self.a:
            self.a[i]=int(input("Enter marks for subject"))
    def result(self):
        for ele in range(0,len(self.a)): 
            self.res=self.res+self.a[ele]
        self.res= self.res%5
        print("Percentage",self.res)

a1=reportcard()
a1.inputd()
a1.result()