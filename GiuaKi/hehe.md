Tuyệt vời Khanh! Đây là **bảng tổng hợp công thức RDD thường dùng trong bài kiểm tra thực hành**, giúp bạn nhớ nhanh, làm nhanh, không bị bí:

---

## **TỔNG HỢP CÔNG THỨC RDD THƯỜNG GẶP TRONG THI THỰC HÀNH**

### **1. Loại bỏ dòng header**
```python
header = rdd.first()
data = rdd.filter(lambda x: x != header)
```

---

### **2. Đếm số lượng theo nhóm (ví dụ: số lần mỗi môn xuất hiện)**
```python
data.map(lambda x: (x.split()[4], 1)) \
    .reduceByKey(lambda a, b: a + b)
```

---

### **3. Tính tổng theo nhóm**
```python
data.map(lambda x: (x.split()[4], float(x.split()[6]))) \
    .reduceByKey(lambda a, b: a + b)
```

---

### **4. Tính trung bình theo nhóm (phải dùng `groupByKey()` hoặc đếm kèm tổng)**
**Cách 1 – Dễ hiểu, dùng groupByKey:**
```python
data.map(lambda x: (x.split()[4], float(x.split()[6]))) \
    .groupByKey() \
    .map(lambda x: (x[0], round(sum(x[1]) / len(x[1]), 2)))
```

**Cách 2 – Tối ưu hơn, dùng reduceByKey với `(tổng, đếm)`**
```python
data.map(lambda x: (x.split()[4], (float(x.split()[6]), 1))) \
    .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1])) \
    .map(lambda x: (x[0], round(x[1][0] / x[1][1], 2)))
```

---

### **5. Tìm max/min theo nhóm**
```python
data.map(lambda x: (x.split()[4], float(x.split()[6]))) \
    .reduceByKey(lambda a, b: max(a, b))  # hoặc min(a, b)
```

---

### **6. Lọc theo điều kiện**
Ví dụ: chỉ lấy dữ liệu của năm 2023
```python
data.filter(lambda x: x.split()[8] == '2023')
```

---

### **7. Gộp theo 2 trường (ví dụ: Subject và Year)**
```python
data.map(lambda x: ((x.split()[4], x.split()[8]), float(x.split()[6])))
```

---

### **8. Tìm năm có FinalResult trung bình cao nhất cho mỗi môn**
```python
avg_by_sub_year = data.map(lambda x: ((x.split()[4], x.split()[8]), float(x.split()[6]))) \
                      .groupByKey() \
                      .map(lambda x: (x[0][0], (x[0][1], sum(x[1]) / len(x[1])))) \
                      .groupByKey() \
                      .map(lambda x: (x[0], max(x[1], key=lambda y: y[1])))
```

---

### **9. Sắp xếp kết quả**
```python
rdd.sortBy(lambda x: x[1], ascending=False)  # sort giảm dần theo value
```

---

## **MẸO GHI NHỚ TÊN CỘT (chỉ số `split()`)**
```
SVID Name Gender Class Subject MidResult FinalResult Semester Year
  0     1     2      3      4       5         6         7       8
```

---

## **Mẹo cuối cùng: Nếu quên gì – in thử ra**
```python
print(data.take(3))  # xem dữ liệu đang ở dạng gì
```

---

Mình có thể gửi bạn file PDF hoặc markdown tổng hợp này để ôn trước khi ngủ nếu bạn cần!  
Muốn mình làm không Khanh?