input="/home/5/zhoufang/5243/lab4/input"
for i in 1 3 5 7 10
do
for j in 1000
do
	time python -O jaccard.py $input/input${j}-${i}gram > jac${j}-${i}gram
	time python -O minhash.py $input/input${j}-${i}gram > min${j}-${i}gram
	python -O mse.py jac${j}-${i}gram min${j}-${i}gram
done
done
