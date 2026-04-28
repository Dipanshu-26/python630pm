# multi-level inheritance 

class GrandFather:
    def __init__(self,gfn,ln):
        self.gfname=gfn
        self.lname = ln

    def displayGName(self):
        print(f"Grand father name = {self.gfname} surname = {self.lname}")        

class Father(GrandFather):
    def __init__(self,gfn,ln,ffn):
        super().__init__(gfn,ln)
        self.ffname = ffn

    def displayFName(self):
        print(f"Father name = {self.ffname} surname = {self.lname}")   

class Son(Father):
    def __init__(self,gfn,ln,ffn,sfn):
        super().__init__(gfn,ln,ffn)
        self.sfname = sfn

    def displaySName(self):
        print(f"Son name = {self.sfname} surname = {self.lname}") 

sn = Son("gopalrao","masalkar","niranjan","aditya")
sn.displayGName()
sn.displayFName()
sn.displaySName()

fn=Father("sureshrao","chawde","nitin")
fn.displayGName()
fn.displayFName()

#herarchical, multiple
