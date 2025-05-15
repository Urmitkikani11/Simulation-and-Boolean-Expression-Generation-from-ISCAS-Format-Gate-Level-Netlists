def parse_netlist(file_path):
    circuit = {}
    fanouts = {}
    primary_inputs = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().replace('‚', ',')  # Fix malformed characters
            parts = line.strip().split(',')
            idx = int(parts[0])
            category = parts[1]
            gate_type = parts[2]

            if category == 'gat':
                input_count = int(parts[4])
                inputs = [int(p) for p in parts[5:5 + input_count]]
                circuit[idx] = {'type': gate_type, 'inputs': inputs}
                if gate_type == 'inpt':
                    primary_inputs.append(idx)

            elif category == 'fan':
                source = int(parts[3])
                fanouts[idx] = source

    # Merge fanouts into the circuit
    for fan, source in fanouts.items():
        if fan not in circuit:
            circuit[fan] = {'type': 'fan', 'inputs': [source]}

    return circuit, primary_inputs

def evaluate_gate(gate_type, inputs):
    if gate_type == 'and':
        return int(all(inputs))
    elif gate_type == 'or':
        return int(any(inputs))
    elif gate_type == 'nand':
        return int(not all(inputs))
    elif gate_type == 'nor':
        return int(not any(inputs))
    elif gate_type == 'not':
        return int(not inputs[0])
    elif gate_type == 'xor':
        return int(inputs[0] ^ inputs[1])
    elif gate_type == 'xnor':
        return int(not (inputs[0] ^ inputs[1]))
    elif gate_type == 'inpt':
        return inputs[0]
    elif gate_type == 'fan':
        return inputs[0]
    else:
        raise ValueError(f"Unknown gate type: {gate_type}")


def simulate_circuit(circuit, primary_inputs, input_values):
    signal_values = {}

    for idx, val in zip(primary_inputs, input_values):
        signal_values[idx] = val

    while len(signal_values) < len(circuit):
        for node, info in circuit.items():
            if node in signal_values:
                continue
            inputs_ready = all(inp in signal_values for inp in info['inputs'])
            if inputs_ready:
                input_vals = [signal_values[inp] for inp in info['inputs']]
                signal_values[node] = evaluate_gate(info['type'], input_vals)

    return signal_values

def build_boolean_expression(circuit, node):
    info = circuit[node]
    gate_type = info['type']

    if gate_type == 'inpt':
        return f"N{node}"
    elif gate_type == 'fan':
        return build_boolean_expression(circuit, info['inputs'][0])

    input_exprs = [build_boolean_expression(circuit, inp) for inp in info['inputs']]

    if gate_type == 'and':
        return '(' + ' & '.join(input_exprs) + ')'
    elif gate_type == 'or':
        return '(' + ' | '.join(input_exprs) + ')'
    elif gate_type == 'nand':
        return '~(' + ' & '.join(input_exprs) + ')'
    elif gate_type == 'nor':
        return '~(' + ' | '.join(input_exprs) + ')'
    else:
        raise ValueError(f"Unknown gate type in expression: {gate_type}")

def find_output_nodes(circuit):
    used_as_input = set()
    for info in circuit.values():
        for inp in info['inputs']:
            used_as_input.add(inp)
    outputs = [node for node in circuit if node not in used_as_input]
    return outputs

if __name__ == "__main__":
    netlist_file = "iscas2.txt"  # Your ISCAS-format netlist file
    circuit, primary_inputs = parse_netlist(netlist_file)

    print(f"Primary inputs found: {primary_inputs}")
    input_values = []

    print("Enter values for primary inputs:")
    for inp in primary_inputs:
        while True:
            try:
                val = input(f"Value for N{inp} (0 or 1): ").strip()
                if val not in ['0', '1']:
                    raise ValueError
                input_values.append(int(val))
                break
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")

    signal_values = simulate_circuit(circuit, primary_inputs, input_values)

    print("\n--- Simulation Output ---")
    for k in sorted(signal_values.keys()):
        print(f"Signal N{k}: {signal_values[k]}")

    output_nodes = find_output_nodes(circuit)

    print("\n--- Boolean Expressions for Output Nets Only ---")
    for node in sorted(output_nodes):
        expr = build_boolean_expression(circuit, node)
        print(f"N{node} = {expr}")
