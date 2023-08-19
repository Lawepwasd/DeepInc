import os


def run_vnnlib(data:int, random:float):
    print(f'now running data {data} in random {random}\n')
    command = f"python3 complete_verifier/abcrown.py --config complete_verifier/5_2_{random}_data{data}.yaml > complete_verifier/result_5_2_{random}_data{data}.txt"
    print(command)
    os.system(command)
    


if __name__ == "__main__":
    for data in [1, 2,3,4,5,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,33,34,35]:
        for random in [0.001, 0.01, 0.03, 0.05]:
            run_vnnlib(data, random)