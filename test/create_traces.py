# ON - OFF type networks
''' Simple script to generate one trace file
    according to bandwidth and time constraints'''
BANDWIDTH_LOW = 0.0
BANDWIDTH_HIGH = 3.0
TIME_LOW = 30
TIME_HIGH = 60

# Open file to write - name according to experiment number
trace = open("exp1","w") 

# flag: 0 ==> LOW ---- 1 ==> HIGH
flag = 0
bandwidth = BANDWIDTH_HIGH

time_list = [0.0]
bw_list = []
bw_list.append(BANDWIDTH_HIGH)
time_steps = 250
count = TIME_HIGH
for i in range(250):
    time_list.append(time_list[i] + 1)
    if (flag == 0 and count == 0):
        bandwidth = BANDWIDTH_LOW
        flag = 1
        count = TIME_LOW
    elif (flag == 1 and count == 0):
        bandwidth = BANDWIDTH_HIGH
        flag = 0
        count = TIME_HIGH
    bw_list.append(bandwidth)
    count -= 1

for i in range(time_steps):
    trace.write('{}\t{}\n'.format(time_list[i], bw_list[i]))