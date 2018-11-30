import pymysql


class ExeMysql:
    def __init__(self):
        self.db = pymysql.connect("localhost", "root",
                                  "021213", "optorun")
        self.cursor = self.db.cursor()

    def  __del__(self):
        self.db.close()

    def query(self):
        sql = "SELECT DISTINCT SerialNo FROM exhaust_nor"  # 查询所有machine
        sql_1 = "SELECT * FROM exhaust_nor WHERE Coater_Style IN ('OTFC-1300D/C')"  # 单镀膜机类型查询(当machine 为 all时查询)
        sql_2 = "SELECT * FROM exhaust_nor WHERE Register_Date BETWEEN \
        '2018-10-31' AND '2018-11-30' AND Coater_Style IN ('OTFC-1300D/C');"   # 镀膜机类型 + 时间范围查询
        sql_3 = "SELECT * FROM exhaust_nor WHERE Coater_Style IN ('OTFC-1300D/C') \
            AND SerialNo IN ('S3238')"  # 镀膜机类型 + Machine Number 查询
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            self.db.commit()
            print("Error: leak rate unable fetch data", e)

    def insert(self, exl_data):
        coater_style = exl_data[0][0]
        serial_no = exl_data[0][1]
        times = exl_data[1]
        exhaust_nor_data = exl_data[2]
        exhaust_150_data = exl_data[3]
        # 三条SQL语句将数据插入三个表
        sql_1 = "INSERT INTO LeakRate (SerialNo,Coater_Style,0_min,1_min,2_min,3_min,4_min,5_min, \
                    6_min,7_min,8_min,9_min,10_min,11_min,12_min,13_min,14_min,15_min, \
          16_min,17_min,18_min,19_min,20_min) values ('%s','%s', \
          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
          %s,%s,%s)" \
                 % (serial_no, coater_style, times[0], times[1], times[2], times[3], times[4],
                    times[5], times[6], times[7], times[8], times[9],
                    times[10], times[11], times[12], times[13], times[14],
                    times[15],times[16], times[17], times[18], times[19], times[20])
        sql_2 = "INSERT INTO Exhaust_nor (SerialNo,Coater_Style,aa,bb,cc,dd,ee,ff,gg," \
              "hh,ii,jj,kk,ll,mm) values ('%s','%s',%s,%s,%s,%s,%s,%s,%s," \
              "%s,%s,%s,%s,%s,%s)" % (serial_no, coater_style, exhaust_nor_data[0], exhaust_nor_data[1],
                                      exhaust_nor_data[2], exhaust_nor_data[3], exhaust_nor_data[4],
                                      exhaust_nor_data[5], exhaust_nor_data[6], exhaust_nor_data[7],
                                      exhaust_nor_data[8], exhaust_nor_data[9], exhaust_nor_data[10],
                                      exhaust_nor_data[11], exhaust_nor_data[12])
        sql_3 = "INSERT INTO Exhaust_150 (SerialNo,Coater_Style,aa,bb,cc,dd,ee,ff,gg," \
              "hh,ii,jj,kk,ll,mm) values ('%s','%s',%s,%s,%s,%s,%s,%s,%s," \
              "%s,%s,%s,%s,%s,%s)" % (serial_no, coater_style, exhaust_150_data[0], exhaust_150_data[1],
                                      exhaust_150_data[2], exhaust_150_data[3], exhaust_150_data[4],
                                      exhaust_150_data[5], exhaust_150_data[6], exhaust_150_data[7],
                                      exhaust_150_data[8], exhaust_150_data[9], exhaust_150_data[10],
                                      exhaust_150_data[11], exhaust_150_data[12])
        sqls = [sql_1, sql_2, sql_3]
        for sql in sqls:
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except Exception as e:
                print("Error: insert data failure", e)


if __name__ == "__main__":
    my_db = ExeMysql()
    print(my_db.query())

