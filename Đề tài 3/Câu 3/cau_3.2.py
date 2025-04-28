from pyspark import SparkContext
sc = SparkContext("local","quzkhanh")
# Doc file
rdd = sc.textFile("/home/quzkhanh/Code/BigData/Đề tài 3/Spark_Titanic.csv")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

# Tach moi dong thanh thanh mang bang dau phay (Xu ly CSV co ban)
rows = data.map(lambda line: line.split(',')) 

#  Trong so cac hanh khach bao nhieu nguoi la Nam, bao nhieu la nu
gender_count = rows.map(lambda x: x[5].lower()).countByValue()
print(f"Male: ",gender_count.get('male',0))
print(f"Male: ",gender_count.get('female',0))

