import random

# Define the FSA for 0(01)*
fsa_001 = {
    'start': {'0': 'q1'},
    'q1': {'0': 'q2', 'accept': None},  # 'accept' to potentially end here
    'q2': {'1': 'q1'},
}
wejcnwjcnwox