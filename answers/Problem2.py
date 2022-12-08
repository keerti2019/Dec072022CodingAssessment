import psycopg2
import os
import datetime


conn = psycopg2.connect(database="postgres", user="postgres", password="BlueSky@143", host="127.0.0.1",
                        port="8002")

cursor = conn.cursor()
cursor.execute('set search_path="myinterview";')
weather_station = []
# Queries
postgres_weather_insert_query = 'INSERT INTO weather_data_records("date_of_day","max_temp_degc","min_temp_degc","amnt_precipation_mm", "weather_station") VALUES (%s,%s,%s,%s,%s) ON CONFLICT (date_of_day, weather_station) DO NOTHING;'
postgres_yield_insert_query = 'INSERT INTO yield_data_records("year","total_harvest_corn_mt") VALUES (%s,%s) ON CONFLICT (year) DO NOTHING;'

totalRecords = 0
print("Start time: {}".format(datetime.datetime.now()))


def read_copy_txt_file_name(path, query, fn):
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split()
            data.append(fn)
            cursor.execute(query, data)
            global totalRecords
            totalRecords += 1
    f.close()


def read_copy_txt_file(path, query):
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split()
            cursor.execute(query, data)
            global totalRecords
            totalRecords += 1
    f.close()


for txtfile in os.listdir(path='../wx_data'):
    if txtfile.endswith(".txt"):
        file_path = f"{os.getcwd()}/../wx_data/{txtfile}"
        f_name = os.path.basename(file_path).split('/')[-1][0:-4]

        read_copy_txt_file_name(file_path, postgres_weather_insert_query, f_name)
        print("File {} is loaded.".format(txtfile))



for txtfile in os.listdir(path='../yld_data'):
    if txtfile.endswith(".txt"):
        file_path = f"{os.getcwd()}/../yld_data/{txtfile}"
        read_copy_txt_file(file_path, postgres_yield_insert_query)

print("End time: {}".format(datetime.datetime.now()))
print("Total Records: {}".format(totalRecords))

conn.commit()
cursor.close()
conn.close()


# Output
# (venv) chandu@Gautams-MBP answers % python3 Problem2.py
# Start time: 2022-12-08 14:54:14.366097
# File USC00257715.txt is loaded.
# File USC00113879.txt is loaded.
# File USC00127935.txt is loaded.
# File USC00112193.txt is loaded.
# File USC00250640.txt is loaded.
# File USC00257070.txt is loaded.
# File USC00114442.txt is loaded.
# File USC00115833.txt is loaded.
# File USC00130133.txt is loaded.
# File USC00132724.txt is loaded.
# File USC00250130.txt is loaded.
# File USC00256970.txt is loaded.
# File USC00116446.txt is loaded.
# File USC00253175.txt is loaded.
# File USC00129113.txt is loaded.
# File USC00134142.txt is loaded.
# File USC00121229.txt is loaded.
# File USC00116526.txt is loaded.
# File USC00259510.txt is loaded.
# File USC00255470.txt is loaded.
# File USC00257515.txt is loaded.
# File USC00258395.txt is loaded.
# File USC00338313.txt is loaded.
# File USC00131402.txt is loaded.
# File USC00118916.txt is loaded.
# File USC00124181.txt is loaded.
# File USC00128036.txt is loaded.
# File USC00126580.txt is loaded.
# File USC00129670.txt is loaded.
# File USC00115943.txt is loaded.
# File USC00124008.txt is loaded.
# File USC00116910.txt is loaded.
# File USC00114108.txt is loaded.
# File USC00127298.txt is loaded.
# File USC00110187.txt is loaded.
# File USC00253365.txt is loaded.
# File USC00251200.txt is loaded.
# File USC00112140.txt is loaded.
# File USC00253615.txt is loaded.
# File USC00255310.txt is loaded.
# File USC00132864.txt is loaded.
# File USC00129511.txt is loaded.
# File USC00118740.txt is loaded.
# File USC00333780.txt is loaded.
# File USC00254900.txt is loaded.
# File USC00255565.txt is loaded.
# File USC00250435.txt is loaded.
# File USC00252020.txt is loaded.
# File USC00138296.txt is loaded.
# File USC00132977.txt is loaded.
# File USC00118147.txt is loaded.
# File USC00250622.txt is loaded.
# File USC00331592.txt is loaded.
# File USC00258915.txt is loaded.
# File USC00250420.txt is loaded.
# File USC00338830.txt is loaded.
# File USC00115515.txt is loaded.
# File USC00120784.txt is loaded.
# File USC00112483.txt is loaded.
# File USC00332098.txt is loaded.
# File USC00116579.txt is loaded.
# File USC00137979.txt is loaded.
# File USC00258480.txt is loaded.
# File USC00258133.txt is loaded.
# File USC00115712.txt is loaded.
# File USC00331152.txt is loaded.
# File USC00335297.txt is loaded.
# File USC00334189.txt is loaded.
# File USC00253660.txt is loaded.
# File USC00137161.txt is loaded.
# File USC00336600.txt is loaded.
# File USC00253715.txt is loaded.
# File USC00338822.txt is loaded.
# File USC00256135.txt is loaded.
# File USC00254440.txt is loaded.
# File USC00132999.txt is loaded.
# File USC00335041.txt is loaded.
# File USC00331541.txt is loaded.
# File USC00135952.txt is loaded.
# File USC00256040.txt is loaded.
# File USC00134735.txt is loaded.
# File USC00123513.txt is loaded.
# File USC00129557.txt is loaded.
# File USC00114198.txt is loaded.
# File USC00252820.txt is loaded.
# File USC00120177.txt is loaded.
# File USC00134894.txt is loaded.
# File USC00130600.txt is loaded.
# File USC00137147.txt is loaded.
# File USC00116610.txt is loaded.
# File USC00126705.txt is loaded.
# File USC00339312.txt is loaded.
# File USC00336196.txt is loaded.
# File USC00134063.txt is loaded.
# File USC00332119.txt is loaded.
# File USC00120200.txt is loaded.
# File USC00258465.txt is loaded.
# File USC00115326.txt is loaded.
# File USC00338769.txt is loaded.
# File USC00116558.txt is loaded.
# File USC00115079.txt is loaded.
# File USC00253735.txt is loaded.
# File USC00333758.txt is loaded.
# File USC00335315.txt is loaded.
# File USC00252205.txt is loaded.
# File USC00125237.txt is loaded.
# File USC00333375.txt is loaded.
# File USC00338552.txt is loaded.
# File USC00132789.txt is loaded.
# File USC00250375.txt is loaded.
# File USC00138688.txt is loaded.
# File USC00115901.txt is loaded.
# File USC00122149.txt is loaded.
# File USC00114823.txt is loaded.
# File USC00110338.txt is loaded.
# File USC00121873.txt is loaded.
# File USC00123527.txt is loaded.
# File USC00127755.txt is loaded.
# File USC00111436.txt is loaded.
# File USC00110072.txt is loaded.
# File USC00131533.txt is loaded.
# File USC00135769.txt is loaded.
# File USC00135796.txt is loaded.
# File USC00119241.txt is loaded.
# File USC00336781.txt is loaded.
# File USC00254110.txt is loaded.
# File USC00253910.txt is loaded.
# File USC00253630.txt is loaded.
# File USC00126001.txt is loaded.
# File USC00255080.txt is loaded.
# File USC00117551.txt is loaded.
# File USC00121747.txt is loaded.
# File USC00127875.txt is loaded.
# File USC00127646.txt is loaded.
# File USC00111280.txt is loaded.
# File USC00121425.txt is loaded.
# File USC00129253.txt is loaded.
# File USC00250070.txt is loaded.
# File USC00252840.txt is loaded.
# File USC00116738.txt is loaded.
# File USC00253035.txt is loaded.
# File USC00130112.txt is loaded.
# File USC00338534.txt is loaded.
# File USC00115768.txt is loaded.
# File USC00131635.txt is loaded.
# File USC00251145.txt is loaded.
# File USC00252100.txt is loaded.
# File USC00119354.txt is loaded.
# File USC00113335.txt is loaded.
# File USC00256570.txt is loaded.
# File USC00124837.txt is loaded.
# File USC00112348.txt is loaded.
# File USC00332791.txt is loaded.
# File USC00336118.txt is loaded.
# File USC00129080.txt is loaded.
# File USC00127522.txt is loaded.
# File USC00125337.txt is loaded.
# File USC00123418.txt is loaded.
# File USC00127482.txt is loaded.
# File USC00121030.txt is loaded.
# File USC00253185.txt is loaded.
# File USC00331072.txt is loaded.
# File USC00120676.txt is loaded.
# File USC00127125.txt is loaded.
# File USC00331890.txt is loaded.
# File USC00254985.txt is loaded.
# File USC00259090.txt is loaded.
# End time: 2022-12-08 16:24:11.170293
# Total Records: 1729987

