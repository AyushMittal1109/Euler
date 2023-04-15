import subprocess
import matplotlib.pyplot as plt
import numpy as np

def run_command(command):
    process = subprocess.Popen(' '.join(command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
    return stdout.decode()

x_list = [10, 50, 100, 500, 1000, 50000, 10000, 500000, 100000, 5000000, 1000000]
y_list = []
for val in x_list:    
    op = run_command(['echo {0}'.format(val), '|', 'python3 mapper.py', '|', 'sort -k1,1', '|', 'python3 reducer.py'])
    ev = float(op)
    # Calculate the variance of V
    var_v = np.e ** 2 - np.e

    # Calculate the variance of E(V)
    var_ev = var_v / val

    # Calculate the z-score for the desired confidence level
    z = -0.84

    # Calculate the confidence interval
    ci = ev + z * np.sqrt(var_ev)
    y_list.append(ci)

print(y_list)
plt.title(' the desired confidence level taken as 60%')
plt.xlabel('No. of iterations ->')
plt.ylabel('accuracy ->')
plt.scatter(x_list, y_list)
plt.plot(x_list, y_list)
plt.savefig('confidence_level_plot2.png')