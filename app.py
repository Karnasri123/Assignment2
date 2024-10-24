from flask import Flask, request, jsonify
from ast_handler import create_rule, combine_rules, evaluate_rule
from database import save_rule, get_rules

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule_string')
    ast_rule = create_rule(rule_string)
    save_rule(ast_rule, rule_string)
    return jsonify({"message": "Rule created", "rule_ast": ast_rule})

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    rule_list = request.json.get('rules')
    combined_ast = combine_rules(rule_list)
    return jsonify({"combined_rule_ast": combined_ast})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    ast_json = request.json.get('ast_json')
    user_data = request.json.get('user_data')
    result = evaluate_rule(ast_json, user_data)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
