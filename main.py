class MooreMachine:
    def __init__(self, start_state='A'):
        # state -> {'output': <symbol>, 'trans': {input: next_state}}
        self.states = {
            'A':  {'output': 'A', 'trans': {'0': 'A',  '1': 'B'}},
            'B':  {'output': 'B', 'trans': {'0': 'Ca', '1': 'Da'}},
            'Ca': {'output': 'A', 'trans': {'0': 'Db', '1': 'B'}},
            'Da': {'output': 'B', 'trans': {'0': 'B',  '1': 'Cb'}},
            'Cb': {'output': 'C', 'trans': {'0': 'Db', '1': 'B'}},
            'Db': {'output': 'C', 'trans': {'0': 'B',  '1': 'Cb'}},
            'E':  {'output': 'C', 'trans': {'0': 'Db', '1': 'E'}}
        }
        if start_state not in self.states:
            raise ValueError("Invalid start state")
        self.current_state = start_state

    def reset(self, state='A'):
        if state not in self.states:
            raise ValueError("Invalid state")
        self.current_state = state

    def step(self, symbol):
        """Consume one input symbol, transition and return the output of the NEW state (Moore)."""
        if symbol not in ('0', '1'):
            raise ValueError("Input symbols must be '0' or '1'.")
        next_state = self.states[self.current_state]['trans'][symbol]
        self.current_state = next_state
        return self.states[self.current_state]['output']

    def process(self, input_string, include_initial_output=True):
        """
        Process a binary input string.
        By default returns outputs including the initial state's output,
        then the output after each consumed symbol (length = len(input)+1).
        """
        for ch in input_string:
            if ch not in ('0', '1'):
                raise ValueError("Input string must contain only '0' and '1'.")
        outputs = []
        if include_initial_output:
            outputs.append(self.states[self.current_state]['output'])
        for symbol in input_string:
            out = self.step(symbol)
            outputs.append(out)
        return outputs


if __name__ == "__main__":
    # Define test inputs here (change or add strings as needed)
    test_inputs = [
        "00110",
        "11001",
        "1010110",
        "101111",
    ]

    m = MooreMachine(start_state='A')

    for idx, s in enumerate(test_inputs, 1):
        try:
            # reset to start state before each test
            m.reset('A')
            outputs = m.process(s, include_initial_output=True)
            print(f"Test {idx}: input='{s}'")
            print("  Inputs: ", list(s))
            print("  Outputs:", outputs)  # outputs[0] is output of initial state
            print("  Final state:", m.current_state)
        except ValueError as e:
            print(f"Test {idx}: input='{s}' -> Error: {e}")
