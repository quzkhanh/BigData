from pyspark import SparkContext

sc = SparkContext("local","quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

# trung binh diem final resuilt cua tung mon
avg_final = (data
                .filter(lambda x: len(x.split()) > 6)
                .map(lambda x: (x.split()[4],float(x.split()[6])))
                .groupByKey()
                .map(lambda x: (x[0], round(float(sum(x[1])) / len(x[1]),2)))
                )
print(avg_final.collect())