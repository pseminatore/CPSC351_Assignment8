# Patrick Seminatore
# Diego Valdez
# Thomas McDonald
# Github Repo: pseminatore/CPSC351
# python3 

class DFA:
    def __init__(self, states, alphabet, delta, gamma, start, accepts):
        self.states = set(states)
        self.start = start
        self.delta = delta
        self.gamma = gamma
        self.accepts = set(accepts)
        self.alphabet = set(alphabet)
        self.current_state = start

def simulate(customDFA, w):
    customDFA.current_state = customDFA.start
    for c in w:
        if customDFA.current_state not in customDFA.states:
            break
        if c not in customDFA.alphabet:
            break
        customDFA.current_state = customDFA.delta(customDFA, c)
    if customDFA.current_state in customDFA.accepts:
        print("accept")
    else:
        print("reject")

def delta(customDFA, w):
    if customDFA.current_state == "q0" and w == "0":
        customDFA.gamma.insert(0, 0)
        return "q0"
    if customDFA.current_state == "q0" and w == "1" and len(customDFA.gamma) == 0:
        return "q3"
    if customDFA.current_state == "q0" and w == "1":
        customDFA.gamma.pop(0)
        return "q1"
    if  customDFA.current_state == "q1" and w == "0":
        return "q3"
    if  customDFA.current_state == "q1" and w == "1" and len(customDFA.gamma) == 0:
        return "q3"
    if  customDFA.current_state == "q1" and w == "1":
        customDFA.gamma.pop(0)
        return "q1"
    if  customDFA.current_state == "q0" and w == "L":
        return "q0"
    if  customDFA.current_state == "q1" and w == "L" and len(customDFA.gamma) == 0:
        return "q2"
    if  customDFA.current_state == "q1" and w == "L":
        return "q1"

def main():
    while True:
        stringToTest = input("Enter a string to be tested: ")
        if not stringToTest:
            print("accept")
        else:  
            # L here represents Lambda
            stringToTest = stringToTest + 'L'
            statesSet = {"q0", "q1", "q2"}
            acceptSet = {"q2"}
            alphabet = {"0", "1", "L"}
            gamma = []
            customDFA = DFA(statesSet, alphabet, delta, gamma, "q0", acceptSet)
            simulate(customDFA, stringToTest)

main()