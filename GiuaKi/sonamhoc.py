from pyspark import SparkContext

sc = SparkContext("local","quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

number_Of_Subjects = (data
                      .filter(lambda x: len(x.split()) >= 8 and x.split()[8] == "2023")
                      .map(lambda x: (x.split()[1],1))
                      .reduceByKey(lambda a,b: a+b))

print(number_Of_Subjects.collect())