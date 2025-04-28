# su dung rdd , sau do moi dung dataframe
# import thu vien va khoi tao sparkseassion
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, count_distinct, when 
# khoi tao sparksession
spark = SparkSession.builder.appName("BigData").getOrCreate()

# doc du lieu tu file csv
df = spark.read.csv("data.csv",header=True, inferSchema = True)


# Câu 1: Số người dự thi (đếm số tên duy nhất)

num_people = df.select(count_distinct("Name")).collect()[0][0]
print(f"Số người dự thi: {num_people}") 

# câu 2: số người đưới 20 tuổi
num_under_20_rdd = df.rdd.filter(lambda row: row["Age"] < 20).map(lambda row: row["Name"]).distinct().count()

print(f"Số người dưới 20 tuổi (RDD): {num_under_20_rdd}")
# num_under_25_rdd = df.rdd.filter(lambda row: row[2] < 25 and row[2] > 20).map(lambda row: row["Name"]).distinct().count()
# print(f"Số người dưới 25 và trên 20: {num_under_25_rdd}")
# Hiển thị các người dưới 25 và trên 20 tuổi
# df.filter((col("Age") < 25) & (col("Age") > 20)).select("Name", "Age").distinct().show()

df.filter((col("Age") < 25) & (col("Age") > 20)).select("Class Id", "Name", "Age").distinct().show()
