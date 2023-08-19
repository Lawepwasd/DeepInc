from safety_tool_script import run_safety_tool

for network in ['2_2','2_5','2_7','2_9','3_1','3_2','3_4','3_5','3_6','3_7','3_8','3_9','4_1','4_3','4_4','4_5','4_6','4_7','4_8','4_9','5_1','5_2','5_3','5_4','5_5','5_6','5_7','5_8','5_9']:
    for tool in ['care','prdnn']:
        for property in [1,2,3,4]:
            run_safety_tool(network='2_1', tool=tool,property=property)