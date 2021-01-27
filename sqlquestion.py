import pypyodbc


connection = pypyodbc.connect('Driver={SQL Server}; Server=DESKTOP-4SLECV1; Database=Data_base_first')
cursor = connection.cursor()

mySQLQuery = (
    """
    SELECT id, login, password
    from dbo.User_login
    WHERE password='123'
    """
)
# print(mySQLQuery)
cursor.execute(mySQLQuery)
result = cursor.fetchall()
print(result)
connection.close()
