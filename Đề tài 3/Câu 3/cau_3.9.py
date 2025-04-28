from pyspark import SparkContext
import csv
from io import StringIO

sc = SparkContext("local", "quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/Đề tài 3/Spark_Titanic.csv")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

# Hàm parse dòng CSV
def parse_csv_line(line):
    return next(csv.reader(StringIO(line)))

rows = data.map(parse_csv_line)

# hàm phân loại và thêm cột mới
def add_class_column(row):
    pclass = row[1]
    if pclass == '1':
        label = "vip"
    elif pclass == '2':
        label = 'Luxury'
    else:
        label = 'Normal' 
    return row + [label] # noi them cot vao cuoi dong

# gan cot moi
row_with_class = rows.map(add_class_column)
for row in row_with_class.take(5):
    print(row) 

row_with_class.saveAsTextFile("Câu 3/ketqua3_9.csv")    
sc.stop()         