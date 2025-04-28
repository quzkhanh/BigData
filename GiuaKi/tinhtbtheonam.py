from pyspark import SparkContext

sc = SparkContext("local", "quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

# Tính trung bình FinalResult theo Subject và Year
avg_by_subject_year = (data
                       .filter(lambda x: len(x.split()) > 8)
                       .map(lambda x: ((x.split()[4], x.split()[8]), float(x.split()[6])))  # (Subject, Year), FinalResult
                       .groupByKey()                                                  # Nhóm theo (Subject, Year)
                       .map(lambda x: (x[0], round(sum(x[1]) / len(x[1]), 2) )))      # Tính trung bình, làm tròn

# In kết quả
print("Trung binh FinalResult theo Subject va Year:")
avg_by_subject_year.foreach(print)

sc.stop()