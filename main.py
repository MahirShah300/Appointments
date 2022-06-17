import datetime

class Appointment:

    def mockCreateAppointment(self, year, month, day, name, description, id):
        self.appointmentName = name
        year = int(year)
        month = int(month)
        day = int(day)
        datetime.datetime(int(year), int(month), int(day))
        date1 = datetime.date(year, month, day)
        self.dateOfAppointment = date1
        self.description = description
        self.id = id

    def createAppointment(self, id):
        self.appointmentName = input("What is the name of the task: ")
        isValidDate = False
        while isValidDate == False:
            isValidDate = True
            year = int(input("Enter year: "))
            month = int(input("Enter month (MM): "))
            day = int(input("Enter day (DD): "))

            try:
                datetime.datetime(int(year), int(month), int(day))
            except ValueError:
                print("Input date is not valid. Please try again.")
                isValidDate = False

            if (isValidDate):
                print("Input date is valid ..")
                date1 = datetime.date(year, month, day)
                self.dateOfAppointment = date1


        self.description = input("Description: ")
        self.id = id

    def __str__(self):
        return "Appointment name: {}\tDate: {}\tDescription: {}".format(self.appointmentName,self.dateOfAppointment,self.description)

class AllAppointments:
    def __init__(self):
        self.appointments = []
        self.id = 0

    def addAppointment(self):
        a = Appointment()
        self.id +=1
        a.createAppointment(self.id)
        self.appointments.append(a)

    def addMockAppointment(self, year, month, day, name, description):
        a = Appointment()
        self.id +=1
        a.mockCreateAppointment(year, month, day, name, description, self.id)
        self.appointments.append(a)

    def getMonthAppointments(self):
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (MM): "))
        filters_appointments = list(filter(lambda x: (x.dateOfAppointment.month == month and x.dateOfAppointment.year == year), self.appointments))
        if len(filters_appointments) == 0:
            print("No date for this month")
        else:
            for monthAppointment in filters_appointments:
                print(monthAppointment)

    def getYearAppointments(self):
        year = int(input("Enter year: "))
        filters_appointments = list(filter(lambda x: (x.dateOfAppointment.year == year), self.appointments))
        if len(filters_appointments) == 0:
            print("No date for this year")
        else:
            for yearAppointment in filters_appointments:
                print(yearAppointment)
    def updateAppointment(self):
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (MM): "))
        day = int(input("Enter the day(DD): "))
        filters_appointments = list(filter(lambda x: (x.dateOfAppointment.month == month and x.dateOfAppointment.year == year and x.dateOfAppointment.day == day),self.appointments))
        for i in range(len(filters_appointments)):
            print(str(i+1) + "\t" + str(filters_appointments[i]))
        choice = int(input("Choose which appointment you would like to change? "))
        if choice > 0 or choice < len(filters_appointments)+1:
            index = choice-1
            secondChoice = int(input("1)Everything\n2)Date\n3)Name\n4)Description\nWhat would you like to change? "))
            if secondChoice == 1:
                newAppointment = Appointment()
                newAppointment.createAppointment(filters_appointments[index].id)
                self.appointments[filters_appointments[index].id-1] = newAppointment
                print("Appointment successfully Updated")

    def printAllappointments(self):
        for appointment in self.appointments:
            print(appointment)


        #map_filtered_appointments = list(map(lambda x: (x.dateOfAppointment),filters_appointments))




test = AllAppointments()
test.addMockAppointment("2022", "09", "12", "Dentist", "Dentist booked for 7pm")
test.addMockAppointment("2022", "09", "02", "Doctor", "Doctor booked for 3pm")
test.addMockAppointment("2025", "09", "04", "Interview", "Interview booked for 10am")
test.addMockAppointment("2022", "12", "11", "Doctor", "Doctor booked for 4pm")


menu = True
while menu:
    choice = int(input("1)Print all appointments\n2)Add appointment\n3)Search by Month\n4)Search by Year\n5)Update Appointment\n6)exit:"))
    if choice == 1:
        test.printAllappointments()
    elif choice == 2:
        test.addAppointment()
    elif choice == 3:
        test.getMonthAppointments()
    elif choice == 4:
        test.getYearAppointments()
    elif choice == 5:
        test.updateAppointment()
    elif choice == 6:
        menu = False
    else:
        print("Not a valid choice")
