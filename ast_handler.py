class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.left = left  # Left child
        self.right = right  # Right child
        self.value = value  # Value for operands or operator type

def create_rule(rule_string):
    # Simple parsing of a rule string to a Node for demonstration
    # In production, you would add a full parser to handle conditions properly
    if "AND" in rule_string:
        left_part, right_part = rule_string.split("AND")
        return Node('operator', left=Node('operand', value=left_part.strip()), right=Node('operand', value=right_part.strip()), value='AND')
    elif "OR" in rule_string:
        left_part, right_part = rule_string.split("OR")
        return Node('operator', left=Node('operand', value=left_part.strip()), right=Node('operand', value=right_part.strip()), value='OR')
    return Node('operand', value=rule_string.strip())

def combine_rules(rule_list):
    # Combine rules with 'AND' for simplicity
    combined = create_rule(rule_list[0])
    for rule in rule_list[1:]:
        combined = Node('operator', left=combined, right=create_rule(rule), value='AND')
    return combined

def evaluate_rule(ast_json, user_data):
    def evaluate_node(node, data):
        if node.node_type == 'operand':
            return eval(node.value, {}, data)
        elif node.node_type == 'operator':
            left_eval = evaluate_node(node.left, data)
            right_eval = evaluate_node(node.right, data)
            if node.value == 'AND':
                return left_eval and right_eval
            elif node.value == 'OR':
                return left_eval or right_eval
        return False

    return evaluate_node(ast_json, user_data)
