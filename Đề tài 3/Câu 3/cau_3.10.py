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

# Hàm thêm cột mới
def add_class_column(row):
    sex = row[4].lower()
    sibsp = row[6]
    
    if sex == 'female' and sibsp == '1':
        label = "wife"
    elif sex == 'male':
        label = "husband"
    else:
        label = "Other"
    
    return row + [label]

# Gắn cột mới
row_with_sex = rows.map(add_class_column)

# Hiển thị 10 dòng đầu
for row in row_with_sex.take(10):
    print(row)

# Lưu ra file CSV
row_with_sex.map(lambda row: ','.join(row)) \
            .coalesce(1) \
            .saveAsTextFile("Câu 3/KetQua3.10")

sc.stop()
