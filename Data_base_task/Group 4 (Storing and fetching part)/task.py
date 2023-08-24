class database:
     def __init__(self,name,age,grade) :
        self.name = name
        self.age =age
        self.grade=grade
     def add(self):
          y = str(self.name )
          s= str(self.age )
          c= str(self.grade)
          x=open("database.txt",'w')
          x.write(y+s+c)
         
     def delete(self):
           y = str(self.name )
           s= str(self.age )
           c= str(self.grade)
           word= y+s+c
           x=open("database.txt", 'r+') 
           content = x.read()
           if word in content:
                x.seek(0)
                x.truncate()
           else:
                print('string does not exist in a file')

     def read(self):
          x = open("database.txt","r+")
          print("Output of Read is ")
          print(x.read())
          print()
          x.seek(0)  

     def update(self):
          x = open("database.txt","r+")
          data = x.read()
          data = x.replace(x.read)
          with open(r'database.txt', 'w') as file:
           x.write(data)
          print("Text replaced")


student=database(name='mo',age='12',grade="124")
student.add()
student.delete()
student.read()
   
        
    
