Database = []


class Worker:

    def __init__(self, name, age, houre_rate, number_of_working_hours_month, worker_id):
        self.name = str(name)
        self.age = int(age)
        self.houre_rate = int(houre_rate)
        self.number_of_working_hours_month = int(number_of_working_hours_month)
        self.worker_id = worker_id

    def add_worker(self):
        self.name = input("enter the new worker name : ")
        self.age = int(input("enter the new worker age : "))
        self.houre_rate = int(input("enter the new worker houre work : "))
        days_of_Work = 22
        self.number_of_working_hours_month = self.houre_rate * days_of_Work
        self.worker_id = self.name + '-' + str(self.age)
        new_worker = [self.name, self.age, self.houre_rate, self.number_of_working_hours_month, self.worker_id]
        Database.append(new_worker)
        print(
            'new worker name :', new_worker[0],
            '\nnew worker age :', new_worker[1],
            '\nnew worker houre work :', new_worker[2],
            '\nnew worker houre work per month :', new_worker[3],
            '\nnew the worker id :', new_worker[4],
        )

    def list_workers(self):
        print("The list of workers is:")
        for worker in Database:
            print(
                'the name :', worker[0],
                '\n the age: ', worker[1],
                '\n the houre work: ', worker[2], 'hrs',
                '\n the houre rate per month: ', worker[3], 'hrs',
                '\n worker id :', worker[4]
            )

    def search_worker(self):
        search = input("enter the name to search: ")
        for workers in Database:
            if workers[0] == search:
                print(
                    'the name :', workers[0],
                    '\n the age: ', workers[1],
                    '\n the houre work: ', workers[2], 'hrs',
                    '\n the houre rate per month: ', workers[3], 'hrs',
                    '\n worker id :', workers[4])
            else:
                print("invalid name!")

    def delete_worker(self):
        """Deletes a worker from the database."""
        delete = input("enter the name of the worker: ")
        for workers in Database:
            if workers[0] == delete:
                del (workers[0], workers[1], workers[2])
                print("the worker has been deleted successfully")
            else:
                print("invalid name!")

    def update_worker(self):
        workername = input("enter the worker name to update : ")
        for worker in Database:
            if worker[0] == workername:
                # worker = Database[workername]
                self.name = input("enter the new worker name : ")
                self.age = int(input("enter the new worker age : "))
                self.houre_rate = int(input("enter the new worker houre work : "))
                print("the code has been updated successfully!")
                worker[0] = self.name
                worker[1] = self.age
                worker[2] = self.houre_rate
            else:
                print("The worker ID is not correct!")

    action = input(
        "Choose action to do: \n "
        "[1] add \n"
        " [2] list \n"
        " [3] search \n"
        " [4] delete \n"
        " [5] update \n"
        "  (press q to quit) \n")

    while action != "q":
        if action == "1":
            add_worker(add_worker)
            action = input(
                "Choose action to do: \n "
                "[1] add \n"
                " [2] list \n"
                " [3] search \n"
                " [4] delete \n"
                " [5] update \n"
                "  (press q to quit) \n")
        elif action == "2":
            list_workers(list_workers)
            action = input(
                "Choose action to do: \n "
                "[1] add \n"
                " [2] list \n"
                " [3] search \n"
                " [4] delete \n"
                " [5] update \n"
                "  (press q to quit) \n")
        elif action == "3":
            search_worker(search_worker)
            action = input(
                "Choose action to do: \n "
                "[1] add \n"
                " [2] list \n"
                " [3] search \n"
                " [4] delete \n"
                " [5] update \n"
                "  (press q to quit) \n")
        elif action == "4":
            delete_worker(search_worker)
            action = input(
                "Choose action to do: \n "
                "[1] add \n"
                " [2] list \n"
                " [3] search \n"
                " [4] delete \n"
                " [5] update \n"
                "  (press q to quit) \n")
        elif action == "5":
            update_worker(update_worker)
            action = input(
                "Choose action to do: \n "
                "[1] add \n"
                " [2] list \n"
                " [3] search \n"
                " [4] delete \n"
                " [5] update \n"
                "  (press q to quit) \n")
