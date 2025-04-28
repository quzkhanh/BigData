from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import csv
from io import StringIO

# Tạo SparkContext và StreamingContext mỗi 5 giây xử lý 1 batch
sc = SparkContext("local[2]", "BoltonStatsStreaming")
ssc = StreamingContext(sc, 5)

def parse_line(line):
    return next(csv.reader(StringIO(line)))

def process_rdd(rdd):
    if not rdd.isEmpty():
        parsed = rdd.map(parse_line)
        
        # Lọc các trận có đội Bolton
        bolton_matches = parsed.filter(lambda row: "Bolton" in (row[2], row[3]))
    
        if not bolton_matches.isEmpty():
            # Tổng số bàn Bolton ghi được
            bolton_goals = bolton_matches.map(lambda row: 
                int(row[4]) if row[2] == "Bolton" else int(row[5])
            )


            total_goals = bolton_goals.reduce(lambda x, y: x + y)
            match_count = bolton_matches.count()
            avg_goals = round(total_goals / float(match_count), 2)
            
            print(f"🔥 Bolton: {match_count} trận | Tổng bàn: {total_goals} | Hiệu suất: {avg_goals}")
        else:
            print("ℹ️ Không có trận Bolton trong batch này.")
    else:
        print("⚠️ Batch rỗng!")

# Đọc dữ liệu stream từ thư mục đầu vào
lines = ssc.textFileStream("/home/quzkhanh/Code/BigData/stream_input")
lines.foreachRDD(process_rdd)

# ssc.start()
# ssc.awaitTermination()

ssc.start()
ssc.awaitTerminationOrTimeout(60)  # Dừng sau 60s
ssc.stop(stopSparkContext=True, stopGraceFully=True)
print("✅ Đã xử lý xong tất cả file và dừng stream")

