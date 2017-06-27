#!/usr/bin/python
import os
import re
import sys
import numpy as np
import matplotlib.pyplot as plt

TRAIN_LOSS_PATTERN = r"Iteration (\d+), loss = (\d+\.\d*)"
#TEST_LOSS_PATTERN = r"Iteration (\d+), Testing net \(#0\)\n.*\n.*\n.*\n.* rec_loss = (\d+\.\d+)"
#TEST_LOSS_PATTERN  = r"Iteration (\d+), Testing net \(#0\)\n.*\n.* loss = (\d+\.\d+)"
#TEST_ACC_PATTERN   = r"Iteration (\d+), Testing net \(#0\)\n.* accuracy = (\d+\.\d+)"

def main():
    if len(sys.argv) > 1:
        log_file_name = sys.argv[1]
    else:
        raise("please provide log file to process")

    log_file = open(log_file_name, 'r')
    log_data = log_file.read()
    training_result = re.findall(TRAIN_LOSS_PATTERN,log_data)
    #testing_result = re.findall(TEST_LOSS_PATTERN, log_data)
    #testing_accuracy = re.findall(TEST_ACC_PATTERN, log_data)

    train_iter = []
    train_loss = []
    test_iter = []
    test_loss = []
    test_acc_iter = []
    test_acc = []

   # test_loss_length = len(testing_result[0]) - 1
    for train in training_result:
        train_iter.append(int(train[0]))
        train_loss.append(float(train[1]))
    '''
    for test in testing_result:
        test_iter.append(int(test[0]))
        temp_loss = 0
        for i in range(test_loss_length):
            temp_loss += float(test[i+1])
        test_loss.append(temp_loss)
    '''
    #for test in testing_accuracy:
    #    test_acc_iter.append(int(test[0]))
    #    test_acc.append(float(test[1]))

    #print test_iter
    #print test_loss
    # display
    plt.plot(train_iter, train_loss, 'k', label='Train loss', linewidth=0.75)
    #plt.plot(test_iter, test_loss, 'r', label='Test loss', linewidth=1.0)
    #plt.plot(test_acc_iter, test_acc, 'b', label='Test accuracy', linewidth=1.0)
    plt.legend()
    #plt.minorticks_on()
    plt.ylabel('Loss')
    plt.xlabel('Iteration')
    #plt.yticks(np.arange(0, 2.5, 0.1))
    plt.grid()
    plt.savefig(os.path.join(os.path.dirname(log_file_name), log_file_name) +'.png')


def disp_results(fig, ax1, ax2, loss_iterations, losses, accuracy_iterations, accuracies, accuracies_iteration_checkpoints_ind, fileName, color_ind=0):
    modula = len(plt.rcParams['axes.color_cycle'])
    acrIterations =[]
    top_acrs={}
    if accuracies.size:
        if 	accuracies.size>4:
		    top_n = 4
        else:
            top_n = accuracies.size -1
        temp = np.argpartition(-accuracies, top_n)
        result_indexces = temp[:top_n]
        temp = np.partition(-accuracies, top_n)
        result = -temp[:top_n]
        for acr in result_indexces:
            acrIterations.append(accuracy_iterations[acr])
            top_acrs[str(accuracy_iterations[acr])]=str(accuracies[acr])

        sorted_top4 = sorted(top_acrs.items(), key=operator.itemgetter(1))
        maxAcc = np.amax(accuracies, axis=0)
        iterIndx = np.argmax(accuracies)
        maxAccIter = accuracy_iterations[iterIndx]
        maxIter =   accuracy_iterations[-1]
        consoleInfo = format('\n[%s]:maximum accuracy [from 0 to %s ] = [Iteration %s]: %s ' %(fileName,maxIter,maxAccIter ,maxAcc))
        plotTitle = format('max accuracy(%s) [Iteration %s]: %s ' % (fileName,maxAccIter, maxAcc))
        print (consoleInfo)
        #print (str(result))
        #print(acrIterations)
       # print 'Top 4 accuracies:'
        print ('Top 4 accuracies:'+str(sorted_top4))
        plt.title(plotTitle)
    ax1.plot(loss_iterations, losses, color=plt.rcParams['axes.color_cycle'][(color_ind * 2 + 0) % modula])
    ax2.plot(accuracy_iterations, accuracies, plt.rcParams['axes.color_cycle'][(color_ind * 2 + 1) % modula], label=str(fileName))
    ax2.plot(accuracy_iterations[accuracies_iteration_checkpoints_ind], accuracies[accuracies_iteration_checkpoints_ind], 'o', color=plt.rcParams['axes.color_cycle'][(color_ind * 2 + 1) % modula])
    plt.legend(loc='lower right')



if __name__ == "__main__":
    main()
