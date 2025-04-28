## Giải thích chi tiết code trong file assignment.py

### 1. Tổng quan về file assignment.py
File `assignment.py` sử dụng PySpark để phân tích dữ liệu từ file `data.csv` và trả lời 21 yêu cầu của bài tập Big Data. Chương trình thực hiện các nhiệm vụ sau:

- Đọc dữ liệu từ file `data.csv` (dữ liệu điểm thi học sinh).
- Sử dụng PySpark để phân tích dữ liệu và trả lời 21 câu hỏi, ví dụ: số người dự thi, điểm trung bình các môn, điểm cao nhất, v.v.
- Hiển thị kết quả bằng cách in ra màn hình hoặc hiển thị bảng.

Dữ liệu trong `data.csv` có cấu trúc:
```
ClassID,Name,Age,Gender,Subject,Achievement
12,sheets_three,25,male,chinese,50
12,sheets_three,25,male,math,60
...
```
Các cột:
- `ClassID` (lớp)
- `Name` (tên học sinh)
- `Age` (tuổi)
- `Gender` (giới tính)
- `Subject` (môn học)
- `Achievement` (điểm)

---

### 2. Giải thích code trong assignment.py

#### **Phần 1: Import thư viện và khởi tạo SparkSession**
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, count_distinct, when

# Khởi tạo SparkSession
spark = SparkSession.builder.appName("BigDataAssignment").getOrCreate()
```
##### **Giải thích cú pháp:**
- `SparkSession.builder.appName("BigDataAssignment").getOrCreate()`: Khởi tạo một SparkSession.
- `from pyspark.sql.functions import ...`: Import các hàm tiện ích của PySpark:
  - `col`: Tham chiếu đến một cột trong DataFrame.
  - `avg`, `sum`: Tính trung bình và tổng.
  - `count_distinct`: Đếm số giá trị duy nhất.
  - `when`: Dùng để tạo điều kiện (giống `if` trong SQL).

---

#### **Phần 2: Đọc dữ liệu từ file `data.csv`**
```python
# Đọc dữ liệu từ file CSV
df = spark.read.csv("data.csv", header=True, inferSchema=True)
```
##### **Giải thích cú pháp:**
- `spark.read.csv("data.csv", header=True, inferSchema=True)`: Đọc file CSV với dòng đầu tiên làm header, tự động suy luận kiểu dữ liệu.
- `df`: DataFrame chứa toàn bộ dữ liệu từ `data.csv`.

---

#### **Phần 3: Trả lời các câu hỏi (1-21)**
##### **Câu 1: Số người dự thi (đếm số tên duy nhất)**
```python
num_people = df.select(count_distinct("Name")).collect()[0][0]
print(f"1. Số người dự thi: {num_people}")
```
##### **Giải thích:**
- `count_distinct("Name")`: Đếm số học sinh duy nhất.
- `.collect()[0][0]`: Lấy kết quả từ DataFrame.

##### **Câu 2: Số người dưới 20 tuổi**
```python
num_under_20 = df.filter(col("Age") < 20).select(count_distinct("Name")).collect()[0][0]
print(f"2. Số người dưới 20 tuổi: {num_under_20}")
```
##### **Giải thích:**
- `df.filter(col("Age") < 20)`: Lọc các học sinh dưới 20 tuổi.
- `.select(count_distinct("Name"))`: Đếm số học sinh duy nhất.

##### **Câu 9: Điểm trung bình môn tiếng Trung**
```python
avg_chinese = df.filter(col("Subject") == "chinese").agg(avg("Achievement")).collect()[0][0]
print(f"9. Điểm trung bình môn tiếng Trung: {avg_chinese}")
```
##### **Giải thích:**
- `df.filter(col("Subject") == "chinese")`: Lọc môn học là "chinese".
- `.agg(avg("Achievement"))`: Tính trung bình điểm số.

##### **Câu 15: Điểm trung bình của từng học sinh**
```python
avg_per_student = df.groupBy("Name").agg(avg("Achievement").alias("avg_score"))
print("15. Điểm trung bình của từng học sinh:")
avg_per_student.show()
```
##### **Giải thích:**
- `df.groupBy("Name")`: Nhóm theo tên học sinh.
- `.agg(avg("Achievement").alias("avg_score"))`: Tính điểm trung bình.

##### **Câu 20: Số bạn nữ lớp 12 có tổng điểm trên 150**
```python
total_score_per_student = df.groupBy("Name", "Gender", "ClassID").agg(sum("Achievement").alias("total_score"))
num_female_12_over_150 = total_score_per_student.filter((col("ClassID") == 12) & (col("Gender") == "Female") & (col("total_score") > 150)).count()
print(f"20. Số bạn nữ lớp 12 có tổng điểm trên 150: {num_female_12_over_150}")
```
##### **Giải thích:**
- `df.groupBy("Name", "Gender", "ClassID").agg(sum("Achievement").alias("total_score"))`: Tính tổng điểm từng học sinh.
- `.filter(...)`: Lọc học sinh nữ lớp 12 có tổng điểm trên 150.
- `.count()`: Đếm số học sinh thỏa mãn điều kiện.

##### **Câu 21: Điểm trung bình của học sinh có tổng điểm trên 150, môn Toán >= 70, từ 18-22 tuổi**
```python
filtered_students = total_score_per_student.filter((col("total_score") > 150) & (col("Age") >= 18) & (col("Age") <= 22))
avg_math_students = df.filter((col("Subject") == "math") & (col("Name").isin([row["Name"] for row in filtered_students.collect()])) & (col("Achievement") >= 70))
avg_final = avg_math_students.agg(avg("Achievement")).collect()[0][0]
print(f"21. Điểm trung bình của học sinh có tổng điểm trên 150, môn Toán >= 70, từ 18-22 tuổi: {avg_final}")
```
##### **Giải thích:**
- `filtered_students`: Lọc học sinh có tổng điểm trên 150, từ 18-22 tuổi.
- `avg_math_students`: Lọc học sinh đạt >= 70 điểm môn Toán.
- `avg("Achievement")`: Tính điểm trung bình.

---

### **Kết luận**
- Code trên sử dụng **PySpark** để xử lý và phân tích dữ liệu.
- Các thao tác chính gồm: **đọc dữ liệu, lọc dữ liệu, nhóm dữ liệu, tính toán trung bình/tổng**.
- Hiểu rõ các hàm như `filter()`, `groupBy()`, `agg()`, `count_distinct()`, `collect()` sẽ giúp bạn làm việc hiệu quả với PySpark.