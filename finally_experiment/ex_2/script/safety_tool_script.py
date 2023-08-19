import os


def run_safety_tool(network,property,tool):
    print(f"first running {network} {property}")
    first_command = f'./build/DeepInc ' \
    f'finally_experiment/ex_2/nnet/acasxu/ACASXU_experimental_v2a_{network}.nnet ' \
    f'finally_experiment/properties/acas_property_{property}.txt ' \
    f'--timeout 20000 --summary-file finally_experiment/ex_2/sum_dir/safety_sum_dir/time_sum/sum_origin_{network}_{property}.log1 '\
    f'--search-tree-file finally_experiment/ex_2/search_tree/safety_tree/ACASXU_experimental_v2a_{network}_property_{property}.nnet.searchTree '\
    f'--search-tree-summary-path finally_experiment/ex_2/sum_dir/safety_sum_dir/node_sum/sum_node_{network}_{property}.log1 '\
    f'> finally_experiment/ex_2/result_dir/safety_result_dir/result_origin_{network}_{property}.log1'
    print(f"running {first_command}" )
    os.system(first_command)

    print(f"second running {network} {property} {tool}")
    second_command = f'./build/DeepInc ' \
    f'finally_experiment/ex_2/nnet/repair_model/{tool}_ACASXU_{network}_repair.nnet ' \
    f'finally_experiment/properties/acas_property_{property}.txt ' \
    f'--timeout 20000 --summary-file finally_experiment/ex_2/sum_dir/safety_sum_dir/time_dir/sum_{tool}_{network}_{property}.log2 '\
    f'--search-tree-file finally_experiment/ex_2/search_tree/safety_tree/ACASXU_experimental_v2a_{network}_property_{property}.nnet.searchTree '\
    f'--search-tree-summary-path finally_experiment/ex_2/sum_dir/safety_sum_dir/node_sum/sum_{tool}_{network}_{property}.log2 '\
    f'--incremental-verification > finally_experiment/ex_2/result_dir/safety_result_dir/result_{tool}_{network}_{property}.log2'
    print(f"running {second_command}" )
    os.system(second_command)

if __name__ == '__main__':
    run_safety_tool('2_2','4',tool = 'care')

    