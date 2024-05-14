import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="b8zodtnrolduseqzjbso-mysql.services.clever-cloud.com",
        user="uwjnxhpr209oqite",
        password="W68V3euwhAu1VNsyofXh",
        database="b8zodtnrolduseqzjbso")


def insert_data(cursor, data):
    sql = "INSERT INTO tabla (columna1, columna2) VALUES (%s, %s)"
    cursor.execute(sql, data)
    cursor.connection.commit()


def select_data(cursor):
    cursor.execute("SELECT * FROM tabla")
    return cursor.fetchall()


def delete_data(cursor, id):
    sql = "DELETE FROM tabla WHERE id = %s"
    cursor.execute(sql, (id, ))
    cursor.connection.commit()


def main():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    data_to_insert = ("valor_columna1", "valor_columna2")
    insert_data(cursor, data_to_insert)

    result = select_data(cursor)
    print("Datos en la tabla:")
    for row in result:
        print(row)

    id_to_delete = 1
    delete_data(cursor, id_to_delete)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
