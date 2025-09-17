# """
# Create an employee CRM system in which users(objects) can

# # Add their name
# # Apply for leave

# """

# class Employee_CRM:

#     def add_name(self):

#         print("Name added successfully")

#     def apply_leave(self):

#         print("Leave applied successfully")

# user1 = Employee_CRM()

# user1.add_name()

# user1.apply_leave()

# class Library:

#     def borrow_book(self,book):

#         print(f"{book} borrowed successfully")

#     def return_book(self,book):

#         print(f"{book} returned successfully")

# user1 = Library()

# user1.borrow_book("Harry Potter")

# user1.return_book("Lord Of The Rings")

"""
Create an ATM where users can
# add_details(username,account_num,balance)
# deposit money
# withdraw money
"""
class ATM:

    def add_details(self,username,account_no,balance):

        self.balance = balance

        print("Added successfully")

    def deposit(self,d_amt):

        self.balance = self.balance + d_amt

        print("Amount deposited successfully")

    def withdraw(self,w_amt):

        if w_amt > self.balance:

            print("Insufficient balance")

        else:

            self.balance = self.balance - w_amt

            print("Amount withdrawed successfully")

    def display_balance(self):

        print(f"Your balance is {self.balance}")

user1 = ATM()

user1.add_details(username="Anand",account_no=1234,balance=5000)

user1.deposit(1000)

user1.display_balance()

user1.withdraw(4000)

user1.display_balance()

user1.withdraw(10000)

"""
Create a student marks where students can
# add marks of 3 subjects
# get average of marks
# calculate grade
    # marks > 90 >> "A"
    # marks > 80 and <=90 >> "B"
    # marks < 80 >> "failed"
"""

# class Student_Marks:

#     def add_marks(self,mark1:int,mark2:int,mark3:int):

#         self.mark1 = mark1

#         self.mark2 = mark2

#         self.mark3 = mark3

#         print("Marks added successfully")

#     def average_marks(self):

#         average = (self.mark1 + self.mark2 + self.mark3)/3

#         self.average = average
        
#         print(f"Average is {self.average}")

#     def grade(self):

#         print("Your grade is",end=" ")

#         if self.average > 90:

#             print("A")

#         elif self.average > 80 and self.average <= 90:

#             print("B")
        
#         else:

#             print("FAILED")

# student1 = Student_Marks()

# student1.add_marks(80,50,40)

# student1.average_marks()

# student1.grade()

class Student_Marks:    # When an object is created, constructor will be called automatically

    def __init__(self,mark1:int,mark2:int,mark3:int):

        self.mark1 = mark1

        self.mark2 = mark2

        self.mark3 = mark3

        print("Marks added successfully")

    def average_marks(self):

        average = (self.mark1 + self.mark2 + self.mark3)/3

        self.average = average
        
        print(f"Average is {self.average}")

    def grade(self):

        print("Your grade is",end=" ")

        if self.average > 90:

            print("A")

        elif self.average > 80 and self.average <= 90:

            print("B")
        
        else:

            print("FAILED")

student1 = Student_Marks(90,80,70)

student1.average_marks()

student1.grade()
