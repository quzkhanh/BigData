## Cài đặt Hadoop và PySpark trên Fedora

### 1. Cài đặt Hadoop

#### Bước 1: Cài Java (Yêu cầu cho Hadoop)
Cài OpenJDK 11:
```bash
sudo dnf install java-11-openjdk
```
Kiểm tra phiên bản Java:
```bash
java --version
```
Kết quả nên hiển thị OpenJDK 11 (ví dụ: openjdk 11.0.26).

Thiết lập biến môi trường JAVA_HOME:
Mở file `~/.bashrc`:
```bash
nano ~/.bashrc
```
Thêm dòng:
```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
export PATH=$PATH:$JAVA_HOME/bin
```
Áp dụng thay đổi:
```bash
source ~/.bashrc
```
Kiểm tra:
```bash
echo $JAVA_HOME
```

#### Bước 2: Tải và cài đặt Hadoop
Tải Hadoop 3.3.6:
```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
```
Giải nén và di chuyển:
```bash
tar -xzf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /usr/local/hadoop
```

Thiết lập biến môi trường cho Hadoop:
Mở `~/.bashrc`:
```bash
nano ~/.bashrc
```
Thêm các dòng:
```bash
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_COMMON_HOME=$HADOOP_HOME
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```
Áp dụng:
```bash
source ~/.bashrc
```

Cấu hình file `hadoop-env.sh`:
Mở file:
```bash
nano /usr/local/hadoop/etc/hadoop/hadoop-env.sh
```
Thêm các dòng:
```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_COMMON_HOME=$HADOOP_HOME
```
Lưu và thoát.

#### Bước 3: Kiểm tra Hadoop
Kiểm tra phiên bản Hadoop:
```bash
hadoop version
```
Kết quả nên hiển thị:
```
Hadoop 3.3.6
...
```

#### Bước 4: Sửa lỗi nếu có (như INVALID HADOOP_COMMON_HOME)
Nếu gặp lỗi INVALID HADOOP_COMMON_HOME, kiểm tra:
File `/usr/local/hadoop/lib` có chứa `hadoop-common-3.3.6.jar` không:
```bash
ls /usr/local/hadoop/lib | grep hadoop-common
```
Nếu không có, tải lại Hadoop (lặp lại bước 2).

Đảm bảo quyền truy cập:
```bash
sudo chown -R quzkhanh:quzkhanh /usr/local/hadoop
sudo chmod -R 755 /usr/local/hadoop
```

### 2. Cài đặt PySpark

#### Bước 1: Cài Python và pip
Đảm bảo Python 3 đã được cài:
```bash
python3 --version
```
Kết quả nên hiển thị phiên bản Python (ví dụ: Python 3.13.2).

Cài pip nếu chưa có:
```bash
sudo dnf install python3-pip
```
Kiểm tra pip:
```bash
pip3 --version
```

#### Bước 2: Cài PySpark
Cài PySpark:
```bash
pip3 install pyspark
```
Nếu bạn dùng Python 3.13.2 và gặp lỗi tương thích, thử dùng Python 3.11:
```bash
sudo dnf install python3.11
/usr/bin/python3.11 -m pip install pyspark
```

Kiểm tra PySpark:
```bash
pyspark --version
```
Kết quả nên hiển thị phiên bản PySpark (ví dụ: version 3.5.1).

#### Bước 3: Đảm bảo PySpark nhận diện Hadoop
Đảm bảo biến môi trường `HADOOP_HOME` và `HADOOP_COMMON_HOME` đã được thiết lập (như ở bước cài Hadoop).
Nếu cần, thêm:
```bash
export SPARK_DIST_CLASSPATH=$(hadoop classpath)
```

vào `~/.bashrc` và áp dụng:
```bash
source ~/.bashrc
```

### 3. Chạy code PySpark
Đảm bảo file `data.csv` và `assignment.py` nằm trong thư mục làm việc (ví dụ: `/home/quzkhanh/Code/BigData`).

Chạy file:
```bash
python3 assignment.py
```
Hoặc dùng Jupyter Notebook để chạy tương tác:
```bash
pip3 install jupyter
cd /home/quzkhanh/Code/BigData
jupyter notebook
```
Mở `assignment.py` trong Jupyter và chạy từng cell.

### 4. Tóm tắt ngắn gọn
#### Hadoop:
- Cài Java 11: `sudo dnf install java-11-openjdk`.
- Tải Hadoop 3.3.6: `wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz`.
- Giải nén và di chuyển: `sudo mv hadoop-3.3.6 /usr/local/hadoop`.
- Thiết lập biến môi trường trong `~/.bashrc` và `hadoop-env.sh`.
- Kiểm tra: `hadoop version`.

#### PySpark:
- Cài pip: `sudo dnf install python3-pip`.
- Cài PySpark: `pip3 install pyspark`.
- Kiểm tra: `pyspark --version`.
- Chạy code: `python3 assignment.py` hoặc dùng Jupyter Notebook.

### 5. Làm project nhóm

- **Phân tích điểm thi học sinh:** Mở rộng bài tập hiện tại với dữ liệu lớn hơn (tạo dữ liệu giả lập hoặc tìm trên web), phân tích xu hướng điểm theo độ tuổi, giới tính, lớp học.
- **Dự đoán điểm thi:** Sử dụng PySpark MLlib để xây dựng mô hình dự đoán điểm dựa trên các đặc điểm như tuổi, giới tính, môn học.
- **Xử lý dữ liệu thời gian thực:** Tích hợp Kafka với PySpark để xử lý dữ liệu điểm thi giả lập theo thời gian thực.

### 6. Lưu ý
- Nếu gặp lỗi với Python 3.13.2, dùng Python 3.11 (`sudo dnf install python3.11`).
- Đảm bảo quyền truy cập thư mục `/usr/local/hadoop`.
- Nếu cần chạy trong VSCode, cài extension Jupyter để chạy `assignment.py` dưới dạng notebook.
