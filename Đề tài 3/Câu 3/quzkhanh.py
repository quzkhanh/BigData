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

count = (rows.map(lambda x: x[11]) 
    .filter(lambda x: x != '') 
    .map(lambda x: (x, 1)) 
    .reduceByKey(lambda a, b: a + b) 
    .sortBy(lambda x: x[1], ascending= True))

for ben, soluong in count.collect():
    print(f"Bến {ben}: {soluong} người")
