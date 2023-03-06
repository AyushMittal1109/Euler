#!/bin/bash



hadoop fs -rm -r /euler

hadoop fs -mkdir /euler

hadoop fs -copyFromLocal /home/mittal/matrix/input.txt /euler

hadoop fs -ls /euler

hadoop jar /home/mittal/hadoop-3.3.4/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar -input /euler/input.txt -output /euler/output -file /home/mittal/euler/mapper.py -mapper "python3 mapper.py" -file /home/mittal/euler/reducer.py -reducer "python3 reducer.py"

hadoop fs -cat /euler/output/part-00000