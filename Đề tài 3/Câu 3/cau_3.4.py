# tổng cộng có bao nhiêu hành khách trên chuyến tàu?
from pyspark import SparkContext
sc = SparkContext('local','quzkhanh')

rdd = sc.textFile('/home/quzkhanh/Code/BigData/Đề tài 3/Spark_Titanic.csv')
header = rdd.first()
data = rdd.filter(lambda x: x != header)
# Tách mỗi dòng thành mảng bằng dấu phẩy (xử lý CSV cơ bản)
rows = data.map(lambda line: line.split(','))
# dem so luong tre em nam va tre em nu
boy = rows.filter(lambda x: x[6] != "" and x[5] == "male" and float(x[6]) < 13).count()
girl = rows.filter(lambda x: x[6] != "" and x[5] == "female" and float(x[6]) < 13).count()


print(f"Boy: {boy}")
print(f"Girl: {girl}")



