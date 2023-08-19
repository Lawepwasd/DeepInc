from cProfile import run
import os


def run_safety_ranw(network,property,ranw):
    print(f"marabou running {network} {property}")
    origin_command = f'./build/DeepInc ' \
    f'finally_experiment/ex_1/nnet/ranweight/ACASXU_experimental_v2a_perturb_rate{ranw}_{network}.nnet ' \
    f'finally_experiment/properties/acas_property_{property}.txt ' \
    f'--timeout 20000 --summary-file finally_experiment/ex_1/sum_dir/safety_sum_dir/time_sum/sum_incre_{network}_{property}_{ranw}.log0 '\
    f'> finally_experiment/ex_1/result_dir/safety_result_dir/result_incre_{network}_{property}_{ranw}.log0'
    print(f"running {origin_command}\n" )
    os.system(origin_command)

    print(f"first running {network} {property}")
    first_command = f'./build/DeepInc ' \
    f'finally_experiment/ex_1/nnet/ori/ACASXU_experimental_v2a_{network}.nnet ' \
    f'finally_experiment/properties/acas_property_{property}.txt ' \
    f'--timeout 20000 --summary-file finally_experiment/ex_1/sum_dir/safety_sum_dir/time_sum/sum_origin_{network}_{property}.log1 '\
    f'--search-tree-file finally_experiment/ex_1/search_tree/safety_tree/ACASXU_experimental_v2a_{network}_property_{property}.nnet.searchTree '\
    f'--search-tree-summary-path finally_experiment/ex_1/sum_dir/safety_sum_dir/node_sum/sum_node_{network}_{property}.log1 '\
    f'> finally_experiment/ex_1/result_dir/safety_result_dir/result_origin_{network}_{property}.log1'
    print(f"running {first_command}\n" )
    os.system(first_command)

    print(f"second running {network} {property} {ranw}")
    second_command = f'./build/DeepInc ' \
    f'finally_experiment/ex_1/nnet/ranweight/ACASXU_experimental_v2a_perturb_rate{ranw}_{network}.nnet ' \
    f'finally_experiment/properties/acas_property_{property}.txt ' \
    f'--timeout 20000 --summary-file finally_experiment/ex_1/sum_dir/safety_sum_dir/time_sum/sum_incre_{network}_{property}_{ranw}.log2 '\
    f'--search-tree-file finally_experiment/ex_1/search_tree/safety_tree/ACASXU_experimental_v2a_{network}_property_{property}.nnet.searchTree '\
    f'--search-tree-summary-path finally_experiment/ex_1/sum_dir/safety_sum_dir/node_sum/sum_node_{network}_{property}_{ranw}.log2 '\
    f'--incremental-verification > finally_experiment/ex_1/result_dir/safety_result_dir/result_incre_{network}_{property}_{ranw}.log2'
    print(f"running {second_command}\n" )
    os.system(second_command)

if __name__ == '__main__':
    run_safety_ranw('1_1','4',ranw=0.01)

    