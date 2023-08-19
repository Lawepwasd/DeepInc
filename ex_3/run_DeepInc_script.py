
import os


def run_adv_ranw(ranw,data):   
    print(f"running DeepInc {ranw} {data}")
    command = f'./build/DeepInc ' \
    f'finally_experiment/ex_1/nnet/ranweight/ACASXU_experimental_v2a_perturb_rate{ranw}_5_2.nnet ' \
    f'finally_experiment/ex_3/properties/advproperty_network_data_{data}.txt'
    print(f"running {command}\n" )
    os.system(command)



if __name__ == '__main__':
    run_adv_ranw(ranw=0.03,data=1)
