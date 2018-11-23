import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',database='rough')

def selectdata(qry):
    cursor=conn.cursor()
    sql=qry
    cursor.execute(sql)
    data=cursor.fetchone()
    return data


