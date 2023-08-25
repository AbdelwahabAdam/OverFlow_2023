class Database:
    def __init__(self, ob, type):
        valid_types = ['student', 'teacher', 'worker']
        if type not in valid_types:
            raise ValueError(f"Invalid type. Allowed types: {', '.join(valid_types)}")
        self.ob = ob
        self.type = type

    def add_data(self):
        file1 = open(f"{self.type}.txt","a")
        file1.write(f"{self.ob.list_all()} \n")
        file1.close()
        print(f"{self.type} data was added successfully")

    def list_data(self):
        file1 = open(f"{self.type}.txt","r")
        for i in file1.readlines():
            print(i)
        # return file1.readlines()

    def search_data(self, value):
        with open(f"{self.type}.txt", 'r') as file:
            for line in file:
                if value in line:
                    print(line)

    def delete_data(self, value, flag=1): ##flag = 1,ALL
        x = flag
        with open(f"{self.type}.txt", 'r') as file:
            lines = file.readlines()
        
        if x == 'ALL':
            with open(f"{self.type}.txt", 'w') as file:
                for line in lines:
                        if value not in line:
                            file.write(line)
        else:
            with open(f"{self.type}.txt", 'w') as file:
                for line in lines:
                        if x != 0:
                            if value in line:
                                x-=1
                            else:
                                file.write(line)
                        else:
                            file.write(line)

    def update_data(self, value1, value2):
        old_line = ''
        with open(f"{self.type}.txt", 'r') as file:
            for line in file:
                if value1 in line and value2 in line:
                    old_line = line

        with open(f"{self.type}.txt", 'r') as file:
            lines = file.readlines()

        with open(f"{self.type}.txt", 'w') as file:
            for line in lines:
                    if old_line not in line:
                        file.write(line)
                    else:
                        file.write(str(self.ob.list_all()))