from datetime import datetime
from bancoDeDados import BancoDeDados

class Task:
    def __init__(self) -> None:
        pass
    def createTask(self, description, creatorId) -> None:

        # TODO: Adicionar essas informações no mysql
        # * Por hora, vamos alocar somente na memoria
        self.taskId = None
        self.employeeId = None
        self.dateOfStart = None
        self.dateLimit = datetime.now()
        self.description = description
        self.creatorId = creatorId

    def verifyTaskOwner(self) -> bool:
        # TODO: Verificar se a task já esta alocada para um membro existente, e retorna um True ou False, dependendo se já tem um dono
        # * Fazer request no banco de dados
        if (self.employeeId != None): # ? Quando a task está sem dono
            return False
        return True

    def assignOwner(self, employeeId) -> bool:
        # TODO: adicionar as informações do membro que será responsavel por executa-lá
        try:
            if self.verifyTaskOwner():
                return print("\033[91mError: Você não pode adicionar um membro nessa atividade, pois essa atividade, já tem um membro responsavel.\033[0m")
            self.employeeId = employeeId
            return True
        except:
            return False
        
    def listOfAllTasks(self,db):
        records = db.getAllTask()
        print("====================================")
        print(" ID | Empr | Descrição")
        print("---------------------------")
        for row in records:
            # date_of_start, date_limit,
            task_id,description, employee_id  = row
            
            id_string = f"{task_id:3}"
            emp_string = f"{employee_id:4}" if employee_id is not None else "    "
            print(f"{id_string} | {emp_string} | {description}")
        print("====================================")
    

if __name__=="__main__":
    temp = Task(creatorId="1234567809",description="Adicionar um membro")
    temp.assignOwner("01234")
    print(temp.verifyTaskOwner())
