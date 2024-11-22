import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="<PASSWORD>",
)

def populate(data: dict):
    pass


if __name__ == '__main__':
    populate({})