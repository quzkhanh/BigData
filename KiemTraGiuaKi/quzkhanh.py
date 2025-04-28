from pyspark import SparkContext

sc = SparkContext("local", "quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")
header = rdd.first()
data = rdd.filter(lambda x: x != header)    

# co bao nhieu nu
hsNu = (data
        .filter(lambda x: len(x.split()) >= 2 
                    and x.split()[2] == "Female")
        .map(lambda x: x.split()[1])
        .distinct()
        )


count = hsNu.count()
print("SO hs nu: ")
print(count)
sc.stop()