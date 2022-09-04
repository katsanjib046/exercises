# File: matchingDelimiters.py Implementing the matching delimiters algorith
"""
Module: matchingDelimiters Implements an algorithm to check whether every open bracket has been closed.
Contains is_matched(item).
"""
############# Some Imports ############
from stack import ArrayStack


############ Define Algorithm #########

def is_matched(expr):
    """Returns True if all delimiters are matched, or else False.
    Expression is a string."""
    expr_list = list(expr)
    dictionary = {'(' : ')', '{' : '}', '[' : ']'}
    stack = ArrayStack()
    for item in expr_list:
        if item in dictionary.keys():
            stack.push(dictionary[item])
        elif item in dictionary.values():
            if stack._is_empty():
                return False
            if item != stack.pop():
                return False
    return len(stack) == 0

def is_matched1(expr):
    """Another implementation to return True/False based on whether
    all the delimiters are matched.
    expr is string."""
    stack = ArrayStack()
    lefty ='({['
    righty = ')}]'
    for c in expr:
        if c in lefty:
            stack.push(c)
        elif c in righty:
            if stack._is_empty():
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    return stack._is_empty()

def test_matchingDelimiters():
    """Testing for the first method"""
    assert is_matched('{[{[{}]}]}+3-([()])') == True
    assert is_matched('{[{[{}]}]}+3-[()])') == False
    assert is_matched('{[{[{}]}]}+3-([(])') == False
    assert is_matched('{[{[{}]}]}+3-([()]') == False
    assert is_matched('[{[{}]}]}+3-([()])') == False
    assert is_matched('[2+(3*5)-{6+2}]') == True

def test_matchingDelimiters1():
    """Testing for the second method"""
    assert is_matched1('{[{[{}]}]}+3-([()])') == True
    assert is_matched1('{[{[{}]}]}+3-[()])') == False
    assert is_matched1('{[{[{}]}]}+3-([(])') == False
    assert is_matched1('{[{[{}]}]}+3-([()]') == False
    assert is_matched1('[{[{}]}]}+3-([()])') == False
    assert is_matched1('[2+(3*5)-{6+2}]') == True


############## Testing ################
if __name__ == "__main__":
    test_matchingDelimiters1()
