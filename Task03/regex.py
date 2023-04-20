import re

class Regex:
    def is_number(self, e):
        num_pattern = r'\d*'
        match_num = re.findall(num_pattern, e)

        return match_num[0]

    def is_op(self, e):
        op_pattern = r'[+-\/\*]'
        match_op = re.findall(op_pattern, e)

        return match_op

    def is_sum(self, e):
        return re.findall(r'[+]', e)
    
    def is_sub(self, e):
        return re.findall(r'[-]', e)

    def is_nul(self, e):
        return re.findall(r'[\*]', e)

    def is_div(self, e):
        return re.findall(r'[\/]', e)