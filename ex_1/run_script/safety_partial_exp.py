from safety_partial_script import run_safety_ranw
import os

for net in ['1_1','1_2','1_5','3_3','5_2']:
    for property in [1,2,3,4]:
        for ranw in [0.01,0.03,0.05]:
            for partial_rate in [0.1,0.3,0.5]:
                run_safety_ranw(network=net,property=property,ranw=ranw,partial_rate=partial_rate)