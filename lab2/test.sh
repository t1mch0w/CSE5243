#!/bin/sh

for i in 5 60 120 240 500
do
echo ${i} clusters test
python -O kmeansA.py /home/5/zhoufang/5243/lab2/input ${i}
python -O kmeansB.py /home/5/zhoufang/5243/lab2/input ${i}
python -O hclusterA.py /home/5/zhoufang/5243/lab2/input
python -O hclusterB.py /home/5/zhoufang/5243/lab2/input
python -O hclusterC.py /home/5/zhoufang/5243/lab2/input
python -O hclusterD.py /home/5/zhoufang/5243/lab2/input
done
