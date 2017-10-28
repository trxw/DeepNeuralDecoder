#
# Author: Pooya Ronagh (2017)
# All rights reserved.
#
# 2-hidden layer NN in TensorFlow
#

import sys
import os
import json
from time import localtime, strftime

sys.path.insert(0, '../CircuitTrainer')
import ExRecCNOT


if __name__ == '__main__':

    with open(sys.argv[1]) as paramfile:
        param = json.load(paramfile)
    with open(sys.argv[2]) as networkfile:
        network = json.load(networkfile)

    output= []
    datafolder= sys.argv[3]

    for filename in os.listdir(datafolder):
        output.append(ExRecCNOT.train(datafolder + filename, param, network))

    outfilename = strftime("%Y-%m-%d-%H-%M-%S", localtime())
    f = open('../Reports/' + outfilename + '.json', 'w')
    f.write(json.dumps(output, indent=2))
    f.close()

