'''
Title           :plot_learning_curve.py
Description     :This script generates learning curves for caffe models
Author          :Adil Moujahid
Date Created    :20160619
Date Modified   :20160619
version         :0.1
usage           :python plot_learning_curve.py model_1_train.log ./caffe_model_1_learning_curve.png
python_version  :2.7.11
'''

import os
import sys
import subprocess
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt

plt.style.use('ggplot')


caffe_path = '/home/ubuntu/caffe/'
model_log_path = sys.argv[1]
learning_curve_path = sys.argv[2]

#Get directory where the model logs is saved, and move to it
model_log_dir_path = os.path.dirname(model_log_path)
os.chdir(model_log_dir_path)

'''
Generating training and test logs
'''
#Parsing training/validation logs
command = caffe_path + 'tools/extra/parse_log.sh ' + model_log_path
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()
#Read training and test logs
train_log_path = model_log_path + '.train'
test_log_path = model_log_path + '.test'
train_log = pd.read_csv(train_log_path, delim_whitespace=True)
test_log = pd.read_csv(test_log_path, delim_whitespace=True)


'''
Making learning curve
'''
fig, ax1 = plt.subplots()

#Plotting training and test losses
train_loss, = ax1.plot(train_log['#Iters'], train_log['TrainingLoss'], color='red',  alpha=.5)
test_loss, = ax1.plot(test_log['#Iters'], test_log['TestLoss'], linewidth=2, color='green')
ax1.set_ylim(ymin=0, ymax=1)
ax1.set_xlabel('Iterations', fontsize=15)
ax1.set_ylabel('Loss', fontsize=15)
ax1.tick_params(labelsize=15)
#Plotting test accuracy
ax2 = ax1.twinx()
test_accuracy, = ax2.plot(test_log['#Iters'], test_log['TestAccuracy'], linewidth=2, color='blue')
ax2.set_ylim(ymin=0, ymax=1)
ax2.set_ylabel('Accuracy', fontsize=15)
ax2.tick_params(labelsize=15)
#Adding legend
plt.legend([train_loss, test_loss, test_accuracy], ['Training Loss', 'Test Loss', 'Test Accuracy'],  bbox_to_anchor=(1, 0.8))
plt.title('Training Curve', fontsize=18)
#Saving learning curve
plt.savefig(learning_curve_path)

'''
Deleting training and test logs
'''
command = 'rm ' + train_log_path
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()

command = command = 'rm ' + test_log_path
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()



