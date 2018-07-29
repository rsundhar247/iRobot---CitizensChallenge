import sqlite3

sqlite_file = 'my_db.sqlite'

def connect(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c

def close(conn):
    conn.commit()
    conn.close()

def get_max_user_id(cursor, print_out=False):
    cursor.execute("SELECT MAX(BANKING_ID) FROM USER_DETAILS")
    rows = cursor.fetchall()
    user_id = rows[0][0]
    if print_out:
        print('\nData: {}'.format(rows))
    return int(user_id)+1

def get_name(cursor, banking_id, print_out=False):
    cursor.execute("SELECT * FROM USER_DETAILS WHERE BANKING_ID = '{}'".format(str(banking_id)))
    rows = cursor.fetchall()
    if print_out:
        print('\nData: {}'.format(rows))
    return rows

def add_name(cursor, banking_id, name, print_out=False):
    successFlag = False
    if get_name(cursor, banking_id, print_out=False):
        successFlag = cursor.execute("UPDATE USER_DETAILS SET NAME = '{}' WHERE BANKING_ID = '{}'".format(name, banking_id))
    else:
        successFlag = cursor.execute("INSERT INTO USER_DETAILS (BANKING_ID, NAME) VALUES ('{}', '{}')".format(banking_id, name))
        
    if print_out:
        print('\nSuccess Flag : {}'.format(successFlag))
    return successFlag

def get_address(cursor, banking_id, print_out=False):
    cursor.execute("SELECT * FROM USER_DETAILS WHERE BANKING_ID = '{}'".format(str(banking_id)))
    rows = cursor.fetchall()
    if print_out:
        print('\nData: {}'.format(rows))
    return rows

def add_address(cursor, banking_id, address, print_out=False):
    successFlag = False
    if get_address(cursor, banking_id, print_out=False):
        successFlag = cursor.execute("UPDATE USER_DETAILS SET ADDRESS = '{}' WHERE BANKING_ID = '{}'".format(address, banking_id))
    else:
        successFlag = cursor.execute("INSERT INTO USER_DETAILS (BANKING_ID, ADDRESS) VALUES ('{}', '{}')".format(banking_id, address))
    if print_out:
        print('\nSuccess Flag : {}'.format(successFlag))
    return successFlag

def get_dob(cursor, banking_id, print_out=False):
    cursor.execute("SELECT * FROM USER_DETAILS WHERE BANKING_ID = '{}'".format(str(banking_id)))
    rows = cursor.fetchall()
    if print_out:
        print('\nData: {}'.format(rows))
    return rows

def add_dob(cursor, banking_id, dob, print_out=False):
    successFlag = False
    if get_dob(cursor, banking_id, print_out=False):
        successFlag = cursor.execute("UPDATE USER_DETAILS SET DOB = '{}' WHERE BANKING_ID = '{}'".format(dob, banking_id))
    else:
        successFlag = cursor.execute("INSERT INTO USER_DETAILS (BANKING_ID, DOB) VALUES ('{}', '{}')".format(banking_id, dob))
    if print_out:
        print('\nSuccess Flag : {}'.format(successFlag))
    return successFlag

def get_doc_details(cursor, banking_id, print_out=False):
    cursor.execute("SELECT * FROM DOCUMENTS_DETAILS WHERE BANKING_ID = '{}'".format(str(banking_id)))
    rows = cursor.fetchall()
    if print_out:
        print('\nData: {}'.format(rows))
    return rows

def add_doc_details(cursor, banking_id, id_type, id_number, print_out=False):
    successFlag = False
    if get_doc_details(cursor, banking_id, print_out=False):
        successFlag = cursor.execute("UPDATE DOCUMENTS_DETAILS SET ID_TYPE = '{}', ID_NUMBER = '{}' WHERE BANKING_ID = '{}'".format(id_type, id_number, banking_id))
    else:
        successFlag = cursor.execute("INSERT INTO DOCUMENTS_DETAILS (BANKING_ID, ID_TYPE, ID_NUMBER) VALUES ('{}', '{}', '{}')".format(banking_id, id_type, id_number))
    if print_out:
        print('\nSuccess Flag : {}'.format(successFlag))
    return successFlag

def get_user_score(cursor, banking_id, print_out=False):
    cursor.execute("SELECT * FROM USER_SCORE WHERE BANKING_ID = {}".format(str(banking_id)))
    rows = cursor.fetchall()
    if print_out:
        print('\nData: {}'.format(rows))
    return rows

def insert_user_score(cursor, banking_id, score, print_out=False):
    successFlag = False
    if get_user_score(cursor, banking_id, print_out=False):
        successFlag = cursor.execute("UPDATE USER_SCORE SET SCORE = '{}' WHERE BANKING_ID = '{}'".format(score, banking_id))
    else:
        successFlag = cursor.execute("INSERT INTO USER_SCORE (BANKING_ID, SCORE) VALUES ('{}', '{}')".format(banking_id, score))
    if print_out:
        print('\nSuccess Flag : {}'.format(successFlag))
    return successFlag

def validate_user_name(cursor, banking_id, name, print_out=False):
    cursor.execute("SELECT * FROM USER_DETAILS WHERE BANKING_ID = '{}' AND NAME = '{}'".format(banking_id, name))
    rows = cursor.fetchall()
    if rows:
        return True
    else:
        return False
    
def validate_address(cursor, banking_id, address, print_out=False):
    cursor.execute("SELECT * FROM USER_DETAILS WHERE BANKING_ID = '{}' AND ADDRESS = '{}'".format(banking_id, address))
    rows = cursor.fetchall()
    if rows:
        return True
    else:
        return False
    
def validate_dob(cursor, banking_id, dob, print_out=False):
    cursor.execute("SELECT * FROM USER_DETAILS WHERE BANKING_ID = '{}' AND DOB = '{}'".format(banking_id, dob))
    rows = cursor.fetchall()
    if rows:
        return True
    else:
        return False