# Names: Annie Stardess Karitonze, Dayeon Kang
# Class: CSC 290
# Hmwk 1

import random
class FSA:
    def __init__(self, states, alphabet, transitions):
        self.states = states  # List of states
        self.alphabet = alphabet  # Alphabet
        self.transitions = transitions  # Dictionary of transitions
        self.start_state = [key for key, value in transitions.items() if value[0].get('start', False)][0]

    def generate_word(self):
        word = ""
        current_state = self.start_state   
        while True:
            if self.transitions[current_state][0].get('accept', False):
                accepting = self.generateBool(p_true=0.3)
                if accepting:
                    return word
            
            list_of_choices = list(self.transitions[current_state])
            if len(list_of_choices)  > 1:
                next_transition = random.choice(list_of_choices)
            else:
                next_transition = list_of_choices[0]
            next_state = next(iter(next_transition.values()))
            next_input = next(iter(next_transition.keys()))
            word += str(next_input)
            current_state = next_state

    def generateBool(self, p_true):
        return random.random() < p_true

def main(): 
    #0(01)*
    first_fsa = FSA(
        states=['q0', 'q1', 'q2'],
        alphabet=['0', '1'],
        transitions={
            'q0': [{'0': 'q1', 'start': True, 'accept': False}],
            'q1': [{'0': 'q2','accept': True}],
            'q2': [{'1': 'q1', 'accept': False}]
        }
    )

    #1(011)*0*
    second_fsa = FSA(
        states=['p0', 'p1', 'p2', 'p3','p4'],
        alphabet=['0', '1'],
        transitions={
            'p0': [{'1': 'p1', 'start': True, 'accept': False}],
            'p1': [{'0': 'p4', 'accept': True}, {'0': 'p2', 'accept': True}],
            'p2': [{'1': 'p3', 'accept': False}],
            'p3': [{'1': 'p1', 'accept': False}],
            'p4': [{'0': 'p4', 'accept': True}]
        }
    )

    # Test generate_word method using the FSAs initialized above.
    num_tests = 5
    print("Testing generate_word method:")
    print("-------------------------------")
    words1 = []
    words2 = []
    for i in range(num_tests):
        word1 = first_fsa.generate_word()
        word2 = second_fsa.generate_word()
        words1.append(word1)
        words2.append(word2)

    print("words from first_fsa: ", str(words1))
    print("words from second_fsa: ", str(words2))

if __name__ == "__main__":
    main()
