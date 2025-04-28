from pyspark import SparkContext
import csv
from io import StringIO

sc = SparkContext("local", "quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/Đề tài 3/Spark_Titanic.csv")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

def parse_csv_line(line):
    return next(csv.reader(StringIO(line)))

rows = data.map(parse_csv_line)

# Lọc dòng có tuổi, rồi ép kiểu float
ages = rows.filter(lambda x: x[5] != '').map(lambda x: float(x[5]))

max_age = ages.max()
min_age = ages.min()

print(f"👵 Max tuổi: {max_age}")
print(f"🧒 Min tuổi: {min_age}")

sc.stop()
