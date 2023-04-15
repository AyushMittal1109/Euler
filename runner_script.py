import sys
import os

jar_file = sys.argv[1]
input_file_path = sys.argv[2]
hadoop_in_dir = sys.argv[3]
hadoop_out_dir = sys.argv[4]
mr_dir = sys.argv[5]

input_file_name = os.path.basename(input_file_path)
hadoop_input_file_path = hadoop_in_dir + input_file_name

# os.system("hadoop fs -rm -r /euler")

# os.system("hadoop fs -mkdir /euler")

os.system("hadoop fs -copyFromLocal " + input_file_path + " " + hadoop_in_dir )

# os.system("hadoop fs -cat /euler/output/part-00000")

mapper = mr_dir
mapper+="mapper.py"

reducer=mr_dir
reducer+="reducer.py"

os.system("hadoop jar "+sys.argv[1]+" -input "+hadoop_input_file_path+" -output "+hadoop_out_dir+" -file "+mapper+" -mapper \"python3 mapper.py\" -file "+reducer+" -reducer \"python3 reducer.py\"")
