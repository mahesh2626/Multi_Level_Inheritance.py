class Parent:
    food="Yes"
    Shopping="Yes"
    work="No"
    
    def bank(self):
        print("Savings amount")

class fchild(Parent):
    
    def clothes(self):
        print("Clothes of first child")
    
    def phone(self):
        print("Phone of first child")
        
class gchild(fchild):
    
    def laptop(self):
        print("Laptop of grand child")
    
    def books(self):
        print("Books of grand child")        

print("For First child food "+fchild.food)
print("For First child Shopping "+fchild.Shopping)
print("The Work for First Child "+fchild.work)   
fc=fchild()
fc.bank()
fc.clothes()
fc.phone()
print(fc.Shopping)

print("For grand child food "+gchild.food)
print("For grand child Shopping "+gchild.Shopping)
print("The Work for grand Child "+gchild.work)   
gc=gchild()
gc.bank()
gc.clothes()
gc.phone()
print(gc.Shopping)
gc.laptop()
gc.books()