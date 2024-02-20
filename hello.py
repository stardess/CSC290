import random

# Define the FSA for 0*
fsa_0_star = {
    'start': {'0': 'start', 'accept': None},  # Loop back to start on '0', or accept to end
}

def generate_word_0_star(fsa, max_length=10):
    current_state = 'start'
    word = ''
    while current_state != 'accept' and len(word) < max_length:
        transitions = fsa[current_state]
        next_action = random.choice(list(transitions.keys()))
        if next_action == 'accept' or len(word) == max_length - 1:
            break  # End the word
        word += next_action
        current_state = transitions[next_action]
    return word

# Generate a word in the language 0*
print(generate_word_0_star(fsa_0_star))