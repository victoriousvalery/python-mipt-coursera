import sys
num_steps = int(sys.argv[1])

for i in range(num_steps, 0, -1):
    print(" " * i, "#" * (num_steps-i))