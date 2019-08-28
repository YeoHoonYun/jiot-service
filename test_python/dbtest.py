import pymysql

con = pymysql.connect(host='183.98.179.130'
                    , user='jiguem'
                    , password='jigeum!'
                    , db='jiot_main'
                    , charset="utf8mb4")

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM DeviceControlMessages")
    print(cur.fetchall())