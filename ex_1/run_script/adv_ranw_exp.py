from adv_ranw_script import run_adv_ranw
import os

for net in ['1_1','1_2','1_5','3_3','5_2']:
    for adv in [0.05,0.075,0.1]:
        for ranw in [0.001,0.01,0.03,0.05]:
            run_adv_ranw(network=net,ranw=ranw,delta = adv)