'''
Authors: Sapir
'''
import math
from functools import reduce
from math import sqrt
import sys
from operator import mul,add

class NegativeNumberError(Exception):
    pass

class student(object):
    def __init__(self,name,dept,year):
        self.name = name
        self.dept = dept
        try:
            self.year = year
            if year != int(year) :
                raise ValueError
            if year < 0:
                raise NegativeNumberError
        except NegativeNumberError:
            print("Negative number as year input.")
            sys.exit(-1)
        except ValueError:
            print("Year type is not an integer.")
            sys.exit(-1)
        
        
    def __str__(self):
        return "{0} {1} {2}".format(type(self).__name__,self.dept,self.name)
 
    def __repr__(self):
        return "{0}('{1}','{2}',{3})".format(type(self).__name__,self.name,self.dept,self.year)    

class UndergraduateStudent(student):
    
    def introduce(self):
        try:
            if 5-self.year < 0:
                raise NegativeNumberError("NegativeNumberError")
            print('I am a student for the first degree in ' + self.dept + ' department, my name is ' + self.name
                    + ' and I will finish my studies in ' + str(5-self.year) +' years')
        except NegativeNumberError:
            print("Negative number in remaining years calculations.")
            sys.exit(1)
class GraduateStudent(student):

    def introduce(self):
        try:
            print('I am a student for the Master degree in ' + self.dept + ' department, my name is Bachelor ' + self.name
                      + ' and I will finish my studies in ' + 4-self.year +' years')
            if 4-self.year < 0:
                raise NegativeNumberError("NegativeNumberError")
        except NegativeNumberError:
            print("Negative number in remaining years calculations.")
            sys.exit(1)
class PhDStudent(student):
    def introduce(self):
        try:
            print('I am a student for the Ph.D. degree in ' + self.dept + ' department, my name is Almost Doctor ' + self.name
                      + ' and I will finish my studies in ' + 3-self.year +' years')
            if 5-self.year < 0:
                raise NegativeNumberError("NegativeNumberError")
        except ValueError:
            print("Negative number in remaining years calculations.")        



def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionary."""
    attributes = {'type':cls['get']('name'),'this':cls }
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
        return bind_method(value, instance)
    def set_value(name, value):
        attributes[name] = value
    instance = {'get': get_value, 'set': set_value}
    return instance

def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value


def make_class(attributes , class_name , base_class=None):
    """Return a new class, which is a dispatch dictionary."""
    
    attributes['name']=class_name
    
    def get_value(arg):
        if arg in attributes:
            return attributes[arg]
        elif base_class is not None:
            return base_class['get'](arg)

    def set_value(arg, value):
        attributes[arg] = value

    def new(*args):
        return init_instance(cls, *args)
    
    def mro(self):
        m_list=[class_name]
        if(base_class==None):
            return m_list
        else:
            return m_list+base_class['get']('mro')(self)
        
    attributes['mro']=mro        
            
    cls = {'get': get_value , 'set': set_value , 'new': new }
    
    return cls

def init_instance(cls, *args):
    """Return a new object with type cls, initialized with args."""
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance


def make_student_class():
    """Return the Account class, which has deposit and withdraw methods."""
    def __init__(self, name , dept , year):
        self['set']('name', name)
        self['set']('dept', dept)
        self['set']('year', year)
    
    return make_class({'__init__': __init__},'Student')

def make_UndergraduateStudent_class():
        """Return the CheckingAccount class, which imposes a $1 withdrawal fee."""
        def introduce(self):
            print('I am a student for the first degree in ' + self['get']('dept') + ' department, my name is ' + self['get']('name')
                  + ' and I will finish my studies in ' + str(5-self['get']('year')) +' years')
        def ___str__(self):
            return 'Bachelor student' + self['get']('name') +'from' + self['get']('dept') +'department' 
        return make_class({'introduce': introduce , '___str__':___str__  },'UndergraduateStudent',make_student_class())
    
    
def make_GraduateStudent_class():
        """Return the CheckingAccount class, which imposes a $1 withdrawal fee."""
        def introduce(self):
            print('I am a student for the Master degree in ' + self['get']('dept') + ' department, my name is Bachelor ' + self['get']('name')
                  + ' and I will finish my studies in ' + 4-self['get']('year') +' years')
        def ___str__(self):
            return 'MSc student' + self['get']('name') +'from' + self['get']('dept') +'department'    
        return make_class({'introduce': introduce , '___str__':___str__  },'GraduateStudent',make_student_class())

    
def make_PhDStudent_class():
        """Return the CheckingAccount class, which imposes a $1 withdrawal fee."""
        def introduce(self):
            print('I am a student for the Ph.D. degree in ' + self['get']('dept') + ' department, my name is Almost Doctor ' + self['get']('name')
                  + ' and I will finish my studies in ' + 3-self['get']('year') +' years')
        def ___str__(self):
            return 'Ph.D. student' + self['get']('name') +'from' + self['get']('dept') +'department'     
        return make_class({'introduce': introduce , '___str__':___str__  },'UndergraduateStudent',make_student_class())
    
    
    
class Time(object):
    def __init__(self,time):
        self.time = time
    def __add__(self, other):
        return self.amount + other.amount
    def __repr__(self):
        return "{}({})".format(type(self).__name__ , str(self.time)) 
    def __sub__(self , other):
        return self.amount - other.amount
    def __str__(self):
        return str(self.time)+ " "+str(type(self).__name__).lower()+"s"
        
class Day(Time):
    @property    
    def amount(self):
        return self.time*24*60

 
       
class Week(Time):
    @property    
    def amount(self):
        return self.time*7*24*60 

  
            
class Hour(Time):
    @property    
    def amount(self):
        return self.time*60  

def isDay(z):
        return type(z)=='Day'

def isWeek(z):
        return type(z)=='Week'
    
def isHour(z):
        return type(z)=='Hour' 
      
  
 
     
def minConvertor(minute , x):
    if(x == 'Day'):
        return Day(int(minute/(60*24)))
    if(x == "Week"):
        return Week(int(minute/(60*24*7)))
    if(x == "Hour"):
        return Hour(int(minute/60))   
     
def apply(operand,x,y):
    sort ={'Hour':1, "Day":2,"Week":3}
    if (sort[type(x).__name__]>sort[type(y).__name__]):
        if(operand == "add"):
            return minConvertor(x + y, type(y).__name__)
        elif(operand == "sub"):
            return minConvertor(x - y, type(y).__name__)
    if(operand=="add"):
        return minConvertor(x+y, type(x).__name__)
    elif(operand=="sub"):
        return minConvertor(x-y, type(x).__name__)
    else:
        print("Illegal operand")
         
def hourCon(obj):
    return minConvertor(obj.amount, 'Hour')
     
coercions={('day','hour'):hourCon,('week','hour'):hourCon}
def coerce_apply(op,x,y):
    if(op=="add"):
        return minConvertor(x+y, 'Hour')
    if(op=="sub"):
        return minConvertor(x-y, 'Hour')


        



print("------------------------------------------------------")

def accumulate_tree(tree,fn):
    if type(tree) != tuple:
        return tree
    return reduce(fn , (accumulate_tree(branch, fn) for branch in tree))
    

def make_account_class():
    """Return the Account class, which has deposit and withdraw methods."""
    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return self['get']('balance')
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        balance = self['get']('balance')
        if amount > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amount)
        return self['get']('balance')
    return make_class({'__init__': __init__, 'deposit': deposit, 
            'withdraw': withdraw, 'interest': 0.02},'Account')

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
    



