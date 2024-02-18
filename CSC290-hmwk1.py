import random

class FSA:
    def __init__(self, states, alphabet, transitions):
        self.states = states  # List of states
        self.alphabet = alphabet  # Alphabet
        self.transitions = transitions  # Dictionary of transitions
        self.start_state = [key for key, value in transitions.items() if value.get('start', False)][0]


    def traverseFSA(self, word):
        current_state = self.start_state   
        for symbol in word:
            if symbol not in self.alphabet:
                return False  # Reject if input symbol is not in the alphabet
            if current_state not in self.transitions or symbol not in self.transitions[current_state]:
                return False  # Reject if no transition defined for current state and input symbol
            current_state = self.transitions[current_state][symbol]
        return current_state in self.transitions and self.transitions[current_state]['accept']  # Accept if final state is accepting state

    def generate_word(self):
        word = ""
        current_state = self.start_state   
        while True:
            # if self.transitions[current_state]['accept']:
            if self.transitions[current_state].get('accept', False):
                accepting = self.generateBool(p_true=0.3)
                if accepting:
                    return word
                else:
                    continue
            possible_transitions = self.transitions[current_state]
            next_input = random.choice(list(possible_transitions.keys()))
            next_state = possible_transitions[next_input]
            word += str(next_input)
            current_state = next_state

    def generateBool(self, p_true):
        return random.random() < p_true

def main():
    states = ['q0', 'q1', 'q2']
    alphabet = [0, 1]
    transitions = {
        'q0': {0: 'q1', 'start': True, 'accept': False},
        'q1': {0: 'q2', 'start': False, 'accept': True},
        'q2': {1: 'q1', 'start': False, 'accept': False}
    }

    first_fsa = FSA(states, alphabet, transitions)

    # Test generate_word method
    num_tests = 5
    print("Testing generate_word method:")
    print("-------------------------------")
    for i in range(num_tests):
        word = first_fsa.generate_word()
        if first_fsa.traverseFSA(word):
            print(f"Test {i + 1}: Word '{word}' accepted by FSA.")
        else:
            print(f"Test {i + 1}: Word '{word}' not accepted by FSA.")

if __name__ == "__main__":
    main()
