import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


folder = './results/'
logs = os.listdir(folder)


bb_means = []
rb_means = []
fixed_means = []
festive_means = []
bola_means = []
rl_means = []
robustMPC_means = []

for log in logs:
    if os.stat(folder + log).st_size != 0:
        row = pd.read_csv(folder + log, sep='\t', header=None, nrows=49)
        if 'BB' in log:
            bb_means.append(np.mean(row[6]))
        elif 'RB' in log:
            rb_means.append(np.mean(row[6]))
        elif 'FIXED' in log:
            fixed_means.append(np.mean(row[6]))
        elif 'FESTIVE' in log:
            festive_means.append(np.mean(row[6]))
        elif 'BOLA' in log:
            bola_means.append(np.mean(row[6]))
        elif 'RL' in log:
            rl_means.append(np.mean(row[6]))
        elif 'robustMPC' in log:
            robustMPC_means.append(np.mean(row[6]))
    else:
        if 'BB' in log:
            bb_means.append(0)
        elif 'RB' in log:
            rb_means.append(0)
        elif 'FIXED' in log:
            fixed_means.append(0)
        elif 'FESTIVE' in log:
            festive_means.append(0)
        elif 'BOLA' in log:
            bola_means.append(0)
        elif 'RL' in log:
            rl_means.append(0)
        elif 'robustMPC' in log:
            robustMPC_means.append(0)

df = pd.DataFrame({
    'bb': bb_means,
    'rb': rb_means,
    'fixed': fixed_means,
    'festive': festive_means,
    'bola': bola_means,
    'rl': rl_means,
    'robustMPC': robustMPC_means,
})


final_average = [np.mean(df['bb']), 
                 np.mean(df['rb']), 
                 np.mean(df['fixed']), 
                 np.mean(df['festive']), 
                 np.mean(df['bola']), 
                 np.mean(df['rl']),
                 np.mean(df['robustMPC'])]


norm = [float(i)/max(final_average) for i in final_average]



norm_df = pd.DataFrame({'algo':['BB', 'RB', 'FIXED', 'FESTIVE', 'BOLA', 'RL', 'robustMPC'], 'Normalized Average Reward': norm})


ax = norm_df.plot.bar(x='algo', y='Normalized Average Reward')
plt.show()