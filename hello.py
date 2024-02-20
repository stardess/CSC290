import random

class FSA:
    def __init__(self, states, alphabet, transitions):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = 'q0'  # Assuming 'q0' is always the start state

    def traverseFSA(self, word):
        current_state = self.start_state
        for symbol in word:
            # Ensure symbol is int if alphabet is [0, 1]
            symbol = int(symbol)  
            if symbol not in self.alphabet or symbol not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state][symbol]
        return 'accept' in self.transitions[current_state]

    def generate_word(self):
        word = ""
        current_state = self.start_state
        while True:
            transitions = self.transitions[current_state]
            if 'accept' in transitions and self.generateBool(p_true=0.6):
                break
            next_input = random.choice([sym for sym in self.alphabet if sym in transitions])
            current_state = transitions[next_input]
            word += str(next_input)
        return word

    def generateBool(self, p_true):
        return random.random() < p_true

def main():
    states = ['q0', 'q1']
    alphabet = [0, 1]
    transitions = {
        'q0': {1: 'q1', 0: 'q0', 'accept': False},
        'q1': {0: 'q1', 1: 'q1', 'accept': True}
    }
    fsa = FSA(states, alphabet, transitions)

    print("Testing generate_word method:")
    for i in range(5):
        word = fsa.generate_word()
        print("Generated word:", word)
        accepted = fsa.traverseFSA(word)
        print(f"Test {i + 1}: Word '{word}' accepted by FSA: {accepted}")

if __name__ == "__main__":
    main()