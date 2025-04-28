from pyspark import SparkContext

sc = SparkContext("local", "quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")
header = rdd.first()
data = rdd.filter(lambda x: x != header)    

diemhk2 = (data
           .filter(lambda x: len(x.split()) > 7 and 
                             x.split()[7] == "2" and 
                             x.split()[5] != "null" and 
                             x.split()[6] != "null")
                            .distinct()
                            )

count = diemhk2.count()
        
print(f"So ban ghi co diem hoc ky 2 khong null: {count}")
sc.stop()