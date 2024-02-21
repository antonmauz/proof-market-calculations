import random
import math
import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
from scipy.stats import lognorm
from scipy.stats import norm
import plotly.graph_objects as go
from scipy.stats import expon

###### General Variables 
cycle = 0 #cycle number
network_reward = 0 #network reward HOW MUCH?
share_prover_to_validator_reward = 0.8 #share of total_reward left for the validator
total_prover_network_reward = network_reward*share_prover_to_validator_reward
total_validator_network_reward = network_reward*(1-share_prover_to_validator_reward)

#Proof verification and generation
CPUH = 8.4 #proof generation cost in CPU-hour
CPUH_price = 0.134012 #CPU-hour cost in USD https://cloud.google.com/compute/all-pricing
proof_generation = CPUH*CPUH_price
cycle_amount_proof_generated = 1

proof_verification = 5*10**5 #zk snark proof verification cost in gas


####### User input
prover_amount = 1 # amount of proovers the user wants the cycles to run
cycle_amount_user_specified = 1 # amount of cycles the user wants to run

# Payments by the user
fee_per_cycle = 0 # fee per cycle the user is willing to pay
transaction_fee =0 # transaction fee the user is willing to pay
prover_amount * cycle_amount_user_specified * fee_per_cycle #maximum fee the user will pay



####### Prover variables 

# Ranking of the prover in the computation speed
prover_rankings= np.zeros(prover_amount)
ranking_prover = 0
share_reward = 0.55 #share of total_reward left for the prover 
prover_network_reward = total_prover_network_reward * (1 - share_reward) * share_reward**ranking_prover
prover_cycle_fee = (cycle_amount_proof_generated * fee_per_cycle)/prover_amount
prover_reward = prover_network_reward + prover_cycle_fee #reward for the prover

####### Validator variables
validator_amount = 1
validator_network_reward = total_validator_network_reward/validator_amount
validatpr_transaction_fee = transaction_fee/validator_amount
validator_reward = validator_network_reward + transaction_fee #reward for the validator


#Maximum fee of the user
prover_amount * cycle_amount_user_specified * fee_per_cycle
# If not enough amount, the fee will be burned, nodes return fail


### key differences in how the User is shown the best guess for the cycles
# possibility 1: the user is shown the best based on the past  

if __name__ == "__main__":
    current_time = 0
