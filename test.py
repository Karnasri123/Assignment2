import unittest
from ast_handler import create_rule, evaluate_rule

class TestRuleEngine(unittest.TestCase):
    def test_create_rule(self):
        rule = "age > 30 AND department = 'Sales'"
        ast_rule = create_rule(rule)
        self.assertIsNotNone(ast_rule)
        self.assertEqual(ast_rule.value, 'AND')

    def test_evaluate_rule(self):
        ast_rule = {
            "node_type": "operator",
            "left": {"node_type": "operand", "value": "age > 30"},
            "right": {"node_type": "operand", "value": "salary > 50000"},
            "value": "AND"
        }
        user_data = {"age": 35, "salary": 60000}
        result = evaluate_rule(ast_rule, user_data)
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()
