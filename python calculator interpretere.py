'''
Authors: Sapir
'''
import math
from functools import reduce
from math import sqrt
import sys
from operator import mul,add



def repl():
    _vars = {}
    class Exp(object):

        def __init__(self, operator, operands):
            self.operator = operator
            self.operands = operands
    
        def __repr__(self):
            return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))
    
        def __str__(self):
            operand_strs = ', '.join(map(str, self.operands))
            return '{0}({1})'.format(self.operator, operand_strs)

    def calc_eval(exp):
        if type(exp) in (int, float):
            return exp
        if type(exp) == Exp:
            arguments = list(map(calc_eval, exp.operands))
            return calc_apply(exp.operator, arguments)
        if type(exp) == str:
            if exp in _vars:
                return calc_eval(_vars["exp"])
            else:
                raise NameError("unbound variable "+ exp)
    
    def calc_apply(operator, args):
        if operator in ('add', '+'):
            return sum(args)
        if operator in ('sub', '-'):
            if len(args) == 0:
                raise TypeError(operator + 'requires at least 1 argument')
            if len(args) == 1:
                return -args[0]
            return sum(args[:1] + [-arg for arg in args[1:]])
        if operator in ('mul', '*'):
            return reduce(mul, args, 1)
        if operator in ('div', '/'):
            if len(args) != 2:
                raise TypeError(operator + ' requires exactly 2 arguments')
            numer, denom = args
            return numer/denom
    
    # Parsing
    
    def calc_parse(line):
        
        tokens = tokenize(line)
        if len(tokens)>2 and tokens[1] == "=":
            execute(tokens)
        else:
            expression_tree = analyze(tokens)
            if len(tokens) > 0:
                raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
            return expression_tree
    
    def tokenize(line):
        spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ').replace('=',' = ')
        return spaced.strip().split()
    
    known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/']
    
    def execute(tokens):
        key = tokens[0]
        tokens = tokens[2:]
        _vars[key] = calc_eval(calc_parse("".join(tokens)))
        
    
    def analyze(tokens):
        assert_non_empty(tokens)
        token = analyze_token(tokens.pop(0))
        if type(token) in (int, float):
            return token
        if token in known_operators:
            if len(tokens) == 0 or tokens.pop(0) != '(':
                raise SyntaxError('expected ( after ' + token)
            return Exp(token, analyze_operands(tokens))
        if token in _vars:
            return (_vars[token])
        else:
            return token
    
    def analyze_operands(tokens):
        assert_non_empty(tokens)
        operands = []
        while tokens[0] != ')':
            if operands and tokens.pop(0) != ',':
                raise SyntaxError('expected ,')
            operands.append(analyze(tokens))
            assert_non_empty(tokens)
        tokens.pop(0)  # Remove )
        return operands
    
    def assert_non_empty(tokens):
        if len(tokens) == 0:
            raise SyntaxError('unexpected end of line')
    
    def analyze_token(token):
        try:
            return int(token)
        except (TypeError, ValueError):
            try:
                return float(token)
            except (TypeError, ValueError):
                return token
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            if expression_tree:
                print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError,NameError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return

repl()
    



