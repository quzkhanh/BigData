from pyspark import SparkContext
sc = SparkContext("local","quzkhanh")

rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

# tinh trung binh diem mon bigdata cua sv

avg_score_student = (data
             .filter(lambda x: len(x.split()) > 5 and x.split()[4] == "BigData")
             .map(lambda x: float(x.split()[6]))) # lay diem tong ket mon hoc

total_score = avg_score_student.reduce(lambda x,y : x + y)
count = avg_score_student.count()
avg = round((total_score / count),2)

print(f"diem trung binh: {avg}")
# stop sc
sc.stop()