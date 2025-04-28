from pyspark import SparkContext
sc = SparkContext("local","quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/Đề tài 3/Spark_Titanic.csv")
header = rdd.first()

data = rdd.filter(lambda x: x != header)
# tach moi dong thanh mang bang dau , ( xu ly file csv co ban)
rows = data.map(lambda row: row.split(','))
# so hanh khach duoi 13 tuoi
kid = rows.filter(lambda x: x[6] != "" and float(x[6]) < 13).count()
print(f"Kid: {kid}")

