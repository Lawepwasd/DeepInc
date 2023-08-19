
import os


def run_adv_ranw(network,ranw,delta):
    print(f"marabou running {network} {ranw} {delta}")
    origin_command = f'./build/DeepInc ' \
    f'finally_experiment/ex_1/nnet/ranweight/ACASXU_experimental_v2a_perturb_rate{ranw}_{network}.nnet ' \
    f'finally_experiment/properties/acas_xu_robustness_test/advproperty_network_{network}_delta_{delta}_data_3.txt ' \
    f'--timeout 20000 --summary-file finally_experiment/ex_1/sum_dir/adv_sum_dir/time_dir/sum_adv_incre_{network}_ranw_{ranw}_delta_{delta}.log0 '\
    f'> finally_experiment/ex_1/result_dir/adv_result_dir/result_incre_{network}_ranw_{ranw}_delta_{delta}.log0'
    print(f"running {origin_command}\n" )
    os.system(origin_command)
    
    print(f"first running {network} {delta}")
    first_command = f'./build/DeepInc ' \
    f'finally_experiment/ex_1/nnet/ori/ACASXU_experimental_v2a_{network}.nnet ' \
    f'finally_experiment/properties/acas_xu_robustness_test/advproperty_network_{network}_delta_{delta}_data_3.txt ' \
    f'--timeout 20000 --summary-file finally_experiment/ex_1/sum_dir/adv_sum_dir/time_dir/sum_origin_{network}_delta_{delta}.log1 '\
    f'--search-tree-file finally_experiment/ex_1/search_tree/adv_tree/adv_ACASXU_experimental_v2a_{network}_delta_{delta}.nnet.searchTree '\
    f'--search-tree-summary-path finally_experiment/ex_1/sum_dir/adv_sum_dir/node_dir/sum_adv_node_{network}_delta_{delta}.log1 '\
    f'> finally_experiment/ex_1/result_dir/adv_result_dir/result_origin_{network}_delta_{delta}.log1'
    print(f"running {first_command}\n" )
    os.system(first_command)

    print(f"second running {network} {ranw} {delta}")
    command = f'./build/DeepInc ' \
    f'finally_experiment/ex_1/nnet/ranweight/ACASXU_experimental_v2a_perturb_rate{ranw}_{network}.nnet ' \
    f'finally_experiment/properties/acas_xu_robustness_test/advproperty_network_{network}_delta_{delta}_data_3.txt ' \
    f'--timeout 20000 --summary-file finally_experiment/ex_1/sum_dir/adv_sum_dir/time_dir/sum_adv_incre_{network}_ranw_{ranw}_delta_{delta}.log2 '\
    f'--search-tree-file finally_experiment/ex_1/search_tree/adv_tree/adv_ACASXU_experimental_v2a_{network}_delta_{delta}.nnet.searchTree '\
    f'--search-tree-summary-path finally_experiment/ex_1/sum_dir/adv_sum_dir/node_dir/sum_adv_incre_{network}_ranw_{ranw}_delta_{delta}.log2 '\
    f'--incremental-verification > finally_experiment/ex_1/result_dir/adv_result_dir/result_incre_{network}_ranw_{ranw}_delta_{delta}.log2'
    print(f"running {command}\n" )
    os.system(command)

if __name__ == '__main__':
    run_adv_ranw('1_1',ranw=0.03,delta=0.075)
