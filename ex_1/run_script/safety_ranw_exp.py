from safety_ranw_script import run_safety_ranw
import os

for net in ['1_1','1_2','1_5','3_3','5_2']:
    for property in [1,2,3,4]:
        for ranw in [0.001,0.01,0.03,0.05]:
            run_safety_ranw(network=net,property=property,ranw=ranw)