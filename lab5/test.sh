for i in 1000 2000 3000 4000 5000
do
echo shuffle the data for $i dimensions
python -O shuffle.py /home/5/zhoufang/5243/submit/input-$i
done

for s in 2 3 5 7 10
do
for c in 2 3 5 7 10
do
for i in 1000 2000 3000 4000 5000
do
echo s=$s,c=$c,#feature=$i
time ./apriori -tr -s$s -c$c -Rappearances.txt ./input-$i-train ./output-$i
time python -O feature.py ./input-$i-test output-$i
done
done
done
