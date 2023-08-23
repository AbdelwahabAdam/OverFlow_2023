class Worker():
    def __init__(self, name, name2, age, age2, hour_rate, hour_rate2, number_of_working_hours_month, number_of_working_hours_month2):
        self.name = name
        self.age = age
        self.hour_rate = hour_rate
        self.number_of_working_hours_month = number_of_working_hours_month
        self.name2 = name2
        self.age2 = age2
        self.hour_rate2 = hour_rate2
        self.number_of_working_hours_month2 = number_of_working_hours_month2
    # def salary(self):
    #     salary = self.hour_rate * 26
    #     return salary
    #
    # def str(self):
    #     return 'the name: {}\n the age: {}\n the hour_rate: {} \n the hour_rate_per_month: ({}) '.format(self.name,
    #                                                                                                      self.age,
    #                                                                                                      self.hour_rate,
    #                                                                                                      self.salary())

    def remove_worker(self):
        worker_name = input("Please enter the name of the worker you want to remove:")

        if worker_name == self.name:
            del(self.name)

        if worker_name == self.name2:
            del(self.name2)

        # else:
        #     print("The username is not correct")




work = Worker(name = 'ibn halal', age = 25, hour_rate = 22.5, number_of_working_hours_month = 185, name2 = 'Mohamed', age2 = 25, hour_rate2 = 22.5, number_of_working_hours_month2 = 156)

work.remove_worker() 