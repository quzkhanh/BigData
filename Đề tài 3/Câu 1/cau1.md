
### 📌 **RDD là gì?**

RDD (Resilient Distributed Dataset) là **tập dữ liệu phân tán, bất biến**, dùng để xử lý song song trong Spark.

👉 Dữ liệu được chia nhỏ, xử lý nhanh, chịu lỗi tốt.

---

### ✅ **3 cách tạo RDD:**

1. **Từ collection trong code (parallelize):**

```scala
val rdd = sc.parallelize(Array(1, 2, 3))

```

1. **Từ file ngoài (textFile):**

```scala
val rdd = sc.textFile("file.txt")

```

1. **Từ RDD khác (transformation):**

```scala
val rdd2 = rdd.map(x => x * 2)

```

---

### ⚙️ Tính chất quan trọng:

- **Immutable** (không thay đổi)
- **Lazy** (chỉ chạy khi cần)
- **Chịu lỗi** (có thể phục hồi)
- **Xử lý song song**

---
