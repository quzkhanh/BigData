from pyspark import SparkContext

sc = SparkContext("local", "quzkhanh")
rdd = sc.textFile("/home/quzkhanh/Code/BigData/GiuaKi/MidTermRDD.txt")

# Loại bỏ header
header = rdd.first()
data = rdd.filter(lambda data: data != header)

# Lấy danh sách tên nam sinh viên không trùng lặp
male_students = (data
                 .filter(lambda x: len(x.strip().split()) > 2 and x.strip().split()[2] == "Male")
                 .map(lambda x: x.strip().split()[1]).distinct())

male_students.foreach(print)

print("ds ngau nhien")
male_st_random = male_students.sample(False, 0.5)
# Lấy 10 phần tử đầu tiên và in trên cùng một dòng
male_list = male_st_random.take(10)
print(" ".join(male.strip() in male_st_random))

sc.stop()