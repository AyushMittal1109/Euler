#!/bin/bash
hadoop fs -rm -r /euler

hadoop fs -mkdir /euler

hadoop fs -copyFromLocal /home/mittal/matrix/input.txt /euler

hadoop fs -cat /euler/output/part-00000

mapper=$5
mapper+="mapper.py"

reducer=$5
reducer+="reducer.py"

hadoop jar $1 -input $2 -output $4 -file $mapper -mapper "python3 mapper.py" -file $reducer -reducer "python3 reducer.py"