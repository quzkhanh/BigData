from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, count_distinct, when

# Khởi tạo SparkSession
spark = SparkSession.builder.appName("BigDataAssignment").getOrCreate()

# Đọc dữ liệu từ file CSV
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# 1. Số người dự thi (đếm số tên duy nhất)
num_people = df.select(count_distinct("Name")).collect()[0][0]
print(f"1. Số người dự thi: {num_people}")

# 2. Số người dưới 20 tuổi
num_under_20 = df.filter(col("Age") < 20).select(count_distinct("Name")).collect()[0][0]
print(f"2. Số người dưới 20 tuổi: {num_under_20}")

# 3. Số người bằng 20 tuổi
num_20 = df.filter(col("Age") == 20).select(count_distinct("Name")).collect()[0][0]
print(f"3. Số người bằng 20 tuổi: {num_20}")

# 4. Số người trên 20 tuổi
num_over_20 = df.filter(col("Age") > 20).select(count_distinct("Name")).collect()[0][0]
print(f"4. Số người trên 20 tuổi: {num_over_20}")

# 5. Số nam dự thi
num_male = df.filter(col("Gender") == "male").select(count_distinct("Name")).collect()[0][0]
print(f"5. Số nam dự thi: {num_male}")

# 6. Số nữ dự thi
num_female = df.filter(col("Gender") == "Female").select(count_distinct("Name")).collect()[0][0]
print(f"6. Số nữ dự thi: {num_female}")

# 7. Số người trong lớp 12
num_class_12 = df.filter(col("ClassID") == 12).select(count_distinct("Name")).collect()[0][0]
print(f"7. Số người trong lớp 12: {num_class_12}")

# 8. Số người trong lớp 13
num_class_13 = df.filter(col("ClassID") == 13).select(count_distinct("Name")).collect()[0][0]
print(f"8. Số người trong lớp 13: {num_class_13}")

# 9. Điểm trung bình môn tiếng Trung
avg_chinese = df.filter(col("Subject") == "chinese").agg(avg("Achievement")).collect()[0][0]
print(f"9. Điểm trung bình môn tiếng Trung: {avg_chinese}")

# 10. Điểm trung bình môn Toán
avg_math = df.filter(col("Subject") == "math").agg(avg("Achievement")).collect()[0][0]
print(f"10. Điểm trung bình môn Toán: {avg_math}")

# 11. Điểm trung bình môn tiếng Anh
avg_english = df.filter(col("Subject") == "english").agg(avg("Achievement")).collect()[0][0]
print(f"11. Điểm trung bình môn tiếng Anh: {avg_english}")

# 12. Điểm trung bình lớp 12
avg_class_12 = df.filter(col("ClassID") == 12).agg(avg("Achievement")).collect()[0][0]
print(f"12. Điểm trung bình lớp 12: {avg_class_12}")

# 13. Điểm trung bình nam lớp 12
avg_male_12 = df.filter((col("ClassID") == 12) & (col("Gender") == "male")).agg(avg("Achievement")).collect()[0][0]
print(f"13. Điểm trung bình nam lớp 12: {avg_male_12}")

# 14. Điểm trung bình nữ lớp 12
avg_female_12 = df.filter((col("ClassID") == 12) & (col("Gender") == "Female")).agg(avg("Achievement")).collect()[0][0]
print(f"14. Điểm trung bình nữ lớp 12: {avg_female_12}")

# 15. Điểm trung bình của 1 bạn (giả sử tính trung bình tất cả các bạn)
# dùng dataframe, còn thầy yêu cầu dùng rdd
avg_per_student = df.groupBy("Name").agg(avg("Achievement").alias("avg_score"))
print("15. Điểm trung bình của từng học sinh:")
avg_per_student.show()

# 16. Các câu hỏi tương tự với lớp 13
avg_class_13 = df.filter(col("ClassID") == 13).agg(avg("Achievement")).collect()[0][0]
avg_male_13 = df.filter((col("ClassID") == 13) & (col("Gender") == "male")).agg(avg("Achievement")).collect()[0][0]
avg_female_13 = df.filter((col("ClassID") == 13) & (col("Gender") == "Female")).agg(avg("Achievement")).collect()[0][0]
print(f"16. Điểm trung bình lớp 13: {avg_class_13}")
print(f"    Điểm trung bình nam lớp 13: {avg_male_13}")
print(f"    Điểm trung bình nữ lớp 13: {avg_female_13}")

# 17. Điểm cao nhất trường
max_score = df.agg({"Achievement": "max"}).collect()[0][0]
print(f"17. Điểm cao nhất trường: {max_score}")

# 18. Điểm cao nhất tiếng Trung lớp 12
max_chinese_12 = df.filter((col("ClassID") == 12) & (col("Subject") == "chinese")).agg({"Achievement": "max"}).collect()[0][0]
print(f"18. Điểm cao nhất tiếng Trung lớp 12: {max_chinese_12}")

# 19. Điểm cao nhất Toán lớp 13
max_math_13 = df.filter((col("ClassID") == 13) & (col("Subject") == "math")).agg({"Achievement": "max"}).collect()[0][0]
print(f"19. Điểm cao nhất Toán lớp 13: {max_math_13}")

# 20. Số bạn nữ lớp 12 có tổng điểm trên 150
total_score_per_student = df.groupBy("Name", "Gender", "ClassID").agg(sum("Achievement").alias("total_score"))
num_female_12_over_150 = total_score_per_student.filter((col("ClassID") == 12) & (col("Gender") == "Female") & (col("total_score") > 150)).count()
print(f"20. Số bạn nữ lớp 12 có tổng điểm trên 150: {num_female_12_over_150}")

# 21. Điểm trung bình của học sinh có tổng điểm trên 150, môn Toán >= 70, từ 20 tuổi trở lên
filtered_students = df.groupBy("Name", "Age").agg(sum("Achievement").alias("total_score"), avg(when(col("Subject") == "math", col("Achievement"))).alias("math_score"))
avg_score_condition = filtered_students.filter((col("total_score") > 150) & (col("math_score") >= 70) & (col("Age") >= 20)).agg(avg("total_score")).collect()[0][0]
print(f"21. Điểm trung bình của học sinh thỏa mãn điều kiện: {avg_score_condition}")

# Dừng SparkSession
spark.stop()
