from pyspark import SparkContext
import csv
from io import StringIO

sc = SparkContext("local","quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/Đề tài 3/Spark_Titanic.csv")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

def parse_csv_line(line):
    return next(csv.reader(StringIO(line)))

rows = data.map(parse_csv_line)

# gia ve trung binh
fares = rows.map(lambda x: x[9]).filter(lambda x: x != '').map(lambda x: float(x))
total_fares = fares.sum()
numberfares = fares.count()
avg_fare = total_fares / numberfares

# do tuoi trung binh
ages = rows.map(lambda x: x[5]).filter(lambda x: x != '').map(lambda x: float(x))
total_age = ages.sum()
numberAge = ages.count()
avg_age = total_age / numberAge

#todo: khach hang NAM mua ve > avg fare && > age
customer = (rows
            .filter(lambda x: x[4].lower() == 'male'
                    and x[5] != '' and x[9] != ''
                    and float(x[5]) > avg_age 
                    and float(x[9]) > avg_fare       ) 
            )
count_cus = customer.count()
print(f"Customer: {count_cus}")

for line in customer.collect():
    print(line[3])

sc.stop()