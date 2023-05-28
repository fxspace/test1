import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-arg1', '-a1',default=0, type=int, required=False)
parser.add_argument('-arg2', '-a2',default=0, type=int, required=False)
argument_list = parser.parse_args()

print(argument_list)