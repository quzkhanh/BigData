from pyspark import SparkContext
import csv
from io import StringIO

sc = SparkContext("local","quzkanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/Đề tài 3/Spark_Titanic.csv")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

def parse_csv_line(line):
    return next(csv.reader(StringIO(line)))

rows = data.map(parse_csv_line)

ages = rows.map(lambda x: x[5]).filter(lambda x: x != '').map(lambda x: float(x))

maxAge = ages.max()
minAge = ages.min()

print(f"Max tuoi: {maxAge}")
print(f"Min tuoi: {minAge}")