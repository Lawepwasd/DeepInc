from run_DeepInc_script import run_adv_ranw
import os

for data in [1,2,3,4,5,6,7,8,9,10,13,15,16,17,18,19,20,21,22,23,24,25,26,27]:
    for ranw in [0.001,0.01,0.03,0.05]:
        run_adv_ranw(ranw=ranw,data = data)