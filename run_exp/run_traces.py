import sys
import os
import subprocess
import numpy as np

RUN_SCRIPT = 'run_video.py'
RANDOM_SEED = 42
RUN_TIME = 320  # sec
MM_DELAY = 40  # millisec


def main():
    trace_path = sys.argv[1]
    abr_algo = sys.argv[2]
    process_id = sys.argv[3]
    ip = sys.argv[4]

    sleep_vec = list(range(1, 10))  # random sleep second [[convert to list in Python 3 as range returns a lazy object instead of list]]

    files = os.listdir(trace_path)
    for f in files:

        while True:

            np.random.shuffle(sleep_vec)
            sleep_time = sleep_vec[int(process_id)]
            
            proc = subprocess.Popen('mm-delay ' + str(MM_DELAY) +
                                    ' mm-link 12mbps ' + trace_path + f +
                                    ' python ' + RUN_SCRIPT + ' ' + ip + ' ' +
                                    abr_algo + ' ' + str(RUN_TIME) + ' ' +
                                    process_id + ' ' + f + ' ' + str(sleep_time),
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            (out, err) = proc.communicate()

            if out == b'done\n':
                break
            else:
                with open('./chrome_retry_log', 'ab') as log:
                    algo = abr_algo + '_' + f + '\n'
                    log.write(algo.encode('utf-8'))
                    log.write(out + b'\n')
                    log.flush()


if __name__ == '__main__':
    main()
