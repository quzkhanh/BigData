from pyspark import SparkContext

sc = SparkContext("local", "quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

# Tính trung bình FinalResult theo Subject và Year
avg_by_subject_year = (
    data
    .filter(lambda x: len(x.split()) > 8)
    .map(lambda x: ((x.split()[4], x.split()[8]), (float(x.split()[6]), 1)))  # ((Subject, Year), (score, 1))
    .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))  # cộng điểm và đếm số lượng
    .map(lambda x: (x[0], round(x[1][0] / x[1][1], 2)))   # tính trung bình
)

# In kết quả
print("Trung binh FinalResult theo Subject va Year:")
avg_by_subject_year.foreach(print)

sc.stop()