class Employee:
    def __init__(self,name,role,password):
        self.name = name
        self.role = role
        self.__password = password
    
    def user_login(self,passw):
        if self.__password == passw:
            return "Logged In succesfully"
        return "Your password is incorrect"
    
    def view_task(self):
        return "Here are the tasks"
    
    def get_pass(self):
        return self.__password
    
class TeamLeader(Employee):
    def assign_tasks(self):
        return "Assigned you a Task DEV"

class Developer(Employee):
    def submit_tasks(self):
        return "Submitted the task now"