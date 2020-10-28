import mysql.connector as ms

db = ms.connect(host='localhost', user='root', passwd='1234', db='csproject', port=3306)

c=db.cursor()

def totalMember():
    c.execute("SELECT COUNT(MNAME) FROM MEMBERS;")
    result = c.fetchall()
    return result[0][0]

def totalBooks():
    c.execute("SELECT COUNT(BNAME) FROM BOOKS;")
    result = c.fetchall()
    return result[0][0]

def haveReturned():
    c.execute("SELECT COUNT(RETURNED), RETURNED FROM MEMBERS GROUP BY RETURNED;")
    result = c.fetchall()
    a = {
        'yes': result[1][0],
        'no':result[0][0]
    }

    return a

def memberInfo(number:int):
    query = "SELECT * FROM MEMBERS WHERE MNO = %s;"%(number)
    c.execute(query)
    result = c.fetchall()[0]

    a = {
        'id':result[0],
        'name':result[1],
        'bno':result[2],
        'doi':result[3],
        'dor':result[4],
        'ret':result[5]
    }

    return a

def memberRemove(number:int):
    query = "DELETE FROM MEMBERS WHERE MNO = %s;"%(number)
    c.execute(query)
    db.commit()

    return True

def memberInsert(number:int, name:str, bno:str, doi, dor, ret:str):
    query = "INSERT INTO MEMBERS (MNO, MNAME, BNO, DOI, DOR, RETURNED) VALUES (%d,%s,%s,%s,%s,%s);"%(number,name,bno,doi,dor,ret)
    c.execute(query)
    db.commit()

    return True
print(memberInsert(12,'Fatema Palmer','T-1','2020-07-06','2020-07-23','YES'))

def allBooks():
    c.execute("SELECT * FROM BOOKS;")
    result = c.fetchall()
    return result