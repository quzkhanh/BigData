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

# fares = rows.map(lambda x: x[9]).filter(lambda x: float(x) > 0)
fares = rows.filter(lambda x: x[9] != '').map(lambda x: float(x[9]))

total_fare = fares.sum()
num = fares.count()
avg_fare = round(total_fare / num,2)

print(f"GIá vé trung bình: ",avg_fare)

sc.stop()
