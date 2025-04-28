from pyspark import SparkContext

sc = SparkContext("local","quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

# laay ds sinh vien trong trong ds
list_students = (data
                    .filter(lambda x: len(x.split()) > 2)
                    .map(lambda x: ((x.split()[0],x.split()[1])))
                    .distinct()
)

list_students.foreach(print)

sc.stop()