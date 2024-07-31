import mysql.connector

class BancoDeDados:
    def __init__(self) -> None:
        self.config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost', 
            'database': 'sistema_de_gerenciamento',
            'raise_on_warnings': True
        }
        self.conn = self.connectToDatabase()

    def connectToDatabase(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
            # print("Conexão Estabelecida com Sucesso")
            return self.conn
        except:
            print("Não foi possivel estabelecer conexão com o banco de dados")
            return False

    def closeConnection(self):
        self.cursor.close()
        pass

    def addObjetcToEmployee(self, name):
        insert_query = f"INSERT INTO empregados (nome) VALUES ('{name}')"
        self.conn._execute_query(insert_query)

        try:
            self.conn.commit()  # Commit the transaction
            return True
        except Exception as err:
            print(f"Inesperado {err=}, {type(err)=}")
            return False

    def updateTask(self, description="", id_employee="", id=""):
        set_clauses = []
        if description != "":
            set_clauses.append(f"descricao = '{description}'")

        if id_employee != "":
            set_clauses.append(f"id_empregado = {id_employee}")

        # Constrói a consulta UPDATE
        update_query = f"""
            UPDATE tarefas
            SET {", ".join(set_clauses)}
            WHERE Id = {id}
        """
        self.conn._execute_query(update_query)

        try:
            self.conn.commit()  # Commit the transaction
            return True
        except Exception as err:
            print(f"Inesperado {err=}, {type(err)=}")
            return False

    def deleteObjectOnEmployee(self, employeeId):
        try:
            deleteQuery = f"DELETE FROM empregados WHERE id ={employeeId}"
            self.conn._execute_query(deleteQuery)
            return True
        except:
            print("Error: Houve algum erro durante a execução da Query.")
            return False 

    def addObjetcToTask(self, description):
        insert_query = f"INSERT INTO tarefas (descricao) VALUES ('{description}')"
        self.conn._execute_query(insert_query)

        try:
            self.conn.commit()  # Commit the transaction
            return True
        except Exception as err:
            print(f"Inesperado {err=}, {type(err)=}")
            return False

    def deleteObjectOnTask(self, taskId):
        deleteQuery = f"DELETE FROM tarefas WHERE id={taskId}"
        self.conn._execute_query(deleteQuery)
        try:
            self.conn.commit()
            print("Tarefa removida com sucesso!!")
            return True
        except:
            print("Error: Houve algum erro durante a execução da Query.")
            return False 
        
    def searchTaskOwner(self, taskId) -> int:
        searchQuery = f"SELECT id_empregado WHERE id={taskId}"
        self.conn._execute_query(searchQuery)
        try:
            self.conn.commit()
            record = self.conn.fetchall()
            for row in record:
                print(row)
            return record
        except:
            return False
        
    def getAllTask(self,):
        self.cursor.execute("SELECT * FROM tarefas")
        records = self.cursor.fetchall()

        if not records:
            print("No tasks found.")
        else:
            print("\nList of Tasks:")
            return records

    def getAllEmployees(self):
        self.cursor.execute("SELECT * FROM empregados")
        records = self.cursor.fetchall()
        for row in records:
            employeeId, supervisorId, nome = row
            print("-----------------------------")
            print(f"Employee ID: {employeeId}")
            print(f"Supervisor Id: {supervisorId}")
            print(f"Nome do Empregado: {nome}")
            # print("-----------------------------")

        if not records:
            print("No Employee found.")
        else:
            print("\nList of Employee:")
            return records


if __name__=="__main__":
    init = BancoDeDados()
    print(init.connectToDatabase())