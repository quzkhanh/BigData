#!/bin/bash
for year in {2015..2020}
do
  cp Championship_${year}.csv ~/Code/BigData/stream_input/
  echo "📁 Đã đưa file Championship_${year}.csv vào stream_input/"
  sleep 5
done
