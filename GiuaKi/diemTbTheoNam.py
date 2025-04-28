from pyspark import SparkContext

sc = SparkContext("local","quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")
header = rdd.first()
data = rdd.filter(lambda x: x != header)

avg_score = (data
                .filter(lambda x: len(x.split()) > 7)
                # (monhoc,namhoc),diemtongket
                .map(lambda x: ((x.split()[4],x.split()[8]),float(x.split()[6])) )
                .groupByKey()
                .map(lambda x: (x[0], round(sum(x[1]) / len(x[1]),2)))
                .sortBy(lambda x: ((x[0][1],x[0][0]),x[1]) )
                )

avg_score.foreach(print)

print("Trung bình FinalResult theo subject year: ")
print(f"{'Subject':<15} {'Year':<6} {'FinalResult':<5}")
print("_" * 40)

for(subject_year, avg) in avg_score.collect():
    subject, year = subject_year
    print(f"{subject:<15} {year:<6} {avg:<5}")



sc.stop()