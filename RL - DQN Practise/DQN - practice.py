
import torch as T
import torch.nn as nn
import torch.nn.funnctional as F
import torch.optim as optim
import numpy as np

class DeepQNetwork(nn.Module):
    def __init__(self,lr,input_dims,fc1_dim,fc2_dims,n_actions):
        super(DeepQNetwork,self).__init__()
