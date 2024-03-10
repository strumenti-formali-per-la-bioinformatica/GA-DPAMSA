import os.path
import platform
import torch
import math

GAP_PENALTY = -4
MISMATCH_PENALTY = -4
MATCH_REWARD = 4
GA_POPULATION_SIZE = 50
GA_NUM_ITERATION = 1
GA_NUM_MOST_FIT_FOR_ITER = 25

#This depend from the training dataset given to the DQN
AGENT_WINDOW_ROW = 3
AGENT_WINDOW_COLUMN = 12

DATASET_ROW = 3
DATASET_COLUMN = 12

NUM_TOTAL_RANGES = (DATASET_ROW / AGENT_WINDOW_ROW) * (DATASET_COLUMN/AGENT_WINDOW_COLUMN)

update_iteration = 128

batch_size = 128
max_episode = 6000
replay_memory_size = 1000

alpha = 0.0001
gamma = 1
epsilon = 0.8
delta = 0.05

decrement_iteration = math.ceil(max_episode * 0.8 / (epsilon // delta))

device_name = "cuda:1" if torch.cuda.is_available() else "cpu"
device = 'cpu'

weight_path_DPAMSA = "./result/weight"
score_path = "./result/score"
report_path_DPAMSA= "./result/reportDPAMSA"
weight_path_DPAMSA = "./result/weightDPAMSA"
weight_path_DPAMSA_GA = "./result/weightDPAMSA_GA"
report_path_DPAMSA_GA= "./result/reportDPAMSA_GA"

if not os.path.exists(score_path):
    os.makedirs(score_path)
if not os.path.exists(weight_path_DPAMSA):
    os.makedirs(weight_path_DPAMSA)
if not os.path.exists(weight_path_DPAMSA_GA):
    os.makedirs(weight_path_DPAMSA_GA)
if not os.path.exists(report_path_DPAMSA):
    os.makedirs(report_path_DPAMSA)
if not os.path.exists(report_path_DPAMSA_GA):
    os.makedirs(report_path_DPAMSA_GA)

assert 0 < batch_size <= replay_memory_size, "batch size must be in the range of 0 to the size of replay memory."
assert alpha > 0, "alpha must be greater than 0."
assert 0 <= gamma <= 1, "gamma must be in the range of 0 to 1."
assert 0 <= epsilon <= 1, "epsilon must be in the range of 0 to 1."
assert 0 <= delta <= epsilon, "delta must be in the range of 0 to epsilon."
assert 0 < decrement_iteration, "decrement iteration must be greater than 0."
