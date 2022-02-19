import mysql.connector
import time
from mysql.connector import errorcode
import logging

logging.basicConfig(level=logging.INFO)
class Demo:
    def __init__(self, database):
        self.database = database
    def create_table(self):
        db_connection = None
        try:
            db_connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database=self.database)
            logging.info("Connection Established Successfully!")
            my_cursor = db_connection.cursor()
            time.sleep(.5)
            t_name = input("Enter the table name to be created : ")
            id = input("Enter first column name : ")
            id_type = input("Data type : ")
            f_name = input("Enter second column name : ")
            f_name_type = input("Data type : ")
            l_name = input("Enter third column name : ")
            l_name_type = input("Data type : ")
            address = input("Enter fourth column name : ")
            address_type = input("Data type : ")
            # (ID Integer, F_NAME text, L_NAME text, ADDRESS text)
            query = f'CREATE TABLE {t_name} ({id} {id_type},{f_name} {f_name_type}, {l_name} {l_name_type} , {address} {address_type})'
            my_cursor.execute(query)
            db_connection.commit()
            logging.info("Table created Successfully")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()
    def insert_data_to_table(self):
        db_connection = None
        try:
            db_connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database=self.database)
            logging.info("Connection Established Successfully!")
            my_cursor = db_connection.cursor()
            time.sleep(0.5)
            t_name = input("Enter the table name in which you want to insert data : ")
            print("Please insert these details to add it to the table :  ")
            id = input("Enter the id of "+t_name+": ")
            f_name = input("Enter the first name of "+t_name+": ")
            l_name = input("Enter the last name of "+t_name+": ")
            add = input("Enter the address of "+t_name+": ")
            query = f'INSERT INTO {t_name} values(%s, %s, %s, %s)'
            val = (id, f_name, l_name, add)
            my_cursor.execute(query, val)
            db_connection.commit()
            db_connection.close()
            logging.info("Data inserted Successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()

    def delete_from_table(self):
        db_connection=None
        try:
            db_connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database=self.database)
            logging.info("Connection Established Successfully!")
            my_cursor = db_connection.cursor()
            time.sleep(1)
            t_name = input("Enter the table name to delete the data : ")
            id = int(input("Enter the ID of the "+t_name+" which u want to delete : "))
            query = f'DELETE FROM {t_name} WHERE ID={id}'
            my_cursor.execute(query)
            db_connection.commit()
            db_connection.close()
            logging.info("Date Deleted Successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()


    def update_table_data(self):
        db_connection=None
        try:
            db_connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database=self.database)
            logging.info("Connection Established Successfully!")
            my_cursor = db_connection.cursor()
            time.sleep(0.5)
            t_name = input("Enter the table name to update table data : ")
            print("Enter details to Update table data : ")
            id = int(input("Enter the "+t_name+" proper Id : "))
            val = input("Enter the value which you want to update : ")
            column_name = input("Enter the column name whose data you want to update : ")
            query = f'UPDATE {t_name} set {column_name} = "{val}" WHERE ID={id}'
            my_cursor.execute(query)
            db_connection.commit()
            db_connection.close()
            logging.info("Data updated Successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()
    def drop_a_table(self):
        db_connection=None
        try:
            db_connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database=self.database)
            logging.info("Connection Established Successfully!")
            my_cursor = db_connection.cursor()
            time.sleep(0.5)
            t_name = input("Enter the table name drop : ")
            query = f'DROP TABLE {t_name}'
            my_cursor.execute(query)
            db_connection.commit()
            db_connection.close()
            logging.info("Table Dropped Successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()


    def show_data_from_table(self):
        db_connection=None
        try:
            db_connection = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database=self.database)
            logging.info("Connection Established Successfully!")
            my_cursor = db_connection.cursor()
            time.sleep(0.5)
            t_name = input("Enter the table name to view data : ")
            query = f'SELECT * FROM {t_name}'
            my_cursor.execute(query)
            data = my_cursor.fetchall()
            for datas in data:
                print(datas)
            db_connection.commit()
            db_connection.close()
            logging.info("Data Displayed Successfully!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.error("Database does not exist")
                print(err)
            else:
                print(err)
        finally:
            if db_connection != None:
                db_connection.close()

database = input("Enter your databse name : ")
while True:
    d = Demo(database)
    user_choice = int(input('''Enter your choice :
    1.CREATE TABLE
    2.INSERT DATA
    3.DELETE FROM TABLE
    4.UPDATE TABLE DATA
    5.DROP A TABLE
    6.SHOW DATA \n'''))

    if user_choice == 1:
        d.create_table()
    elif user_choice == 2:
        d.insert_data_to_table()
    elif user_choice == 3:
        d.delete_from_table()
    elif user_choice == 4:
        d.update_table_data()
    elif user_choice == 5:
        d.drop_a_table()
    elif user_choice == 6:
        d.show_data_from_table()
    else:
        logging.warning("INVALID INPUT......")
    time.sleep(0.5)
    choice = input("Do you want to continue (y/n) : ")
    if choice == 'y' or choice == 'Y':
        continue
    else:
        break
