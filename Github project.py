class student:
    name=""
    id=123
    add=""
    def __init__(self,name,id,add):
        self.name=name
        self.id=id
        self.add=add

class  coarse:
     name=""
     num_of_hours=0
     def __init__(self,name,number):
        self.name=name
        self.num_of_hours=number

ob1=student('wagdy', 5846 ,'wagdy12345')
print(ob1.name)
print(ob1.add)
print(ob1.id)
'''ob2=coarse("is",12)
print(ob2.name)
print(ob2.num_of_hours)
'''