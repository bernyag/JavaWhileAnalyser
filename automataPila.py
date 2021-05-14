from pila import AutomataPila
import re

def automataPila(tokenList):
	states = {'s', 'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'}
	input_alphabet = {'while', '(', 'N', 'O', ')', '{', '}'}
	stack_alphabet = {'1', '(', 'N', '{'}
	transitions = {
	    's': {'while': {'1': (['1'], 'q0')}},
	    'q0': {'(': {'1': (['1', '('], 'q1'),
	                 '{': (['{', '('], 'q1')}}, 
	    'q1': {'N': {'(': (['(', 'N'], 'q2')}}, 
	    'q2': {'O': {'N': (['N'], 'q3')}}, 
	    'q3': {'N': {'N': ([], 'q4')}}, 
	    'q4': {')': {'(': ([], 'q5')}}, 
	    'q5': {'{': {'1': (['1', '{'], 'q6'),
	                 '{': (['{', '{'], 'q6')}}, 
	    'q6': {'while': {'{': (['{'], 'q0')},
	           '}': {'{': ([], 'q7')}}, 
	    'q7': {'}': {'{': ([], 'q7')},
	           '': {'1': ([], 'q8')}}
	}

	tokens = []

	for token in tokenList:
	    if re.fullmatch(r"[a-z0-9]", token):
	        token = 'N'
	    elif re.fullmatch(r"[<>]|==", token):
	        token = 'O'
	    tokens.append(token)
	    
	automata = AutomataPila(states=states, input_alphabet=input_alphabet, stack_alphabet=stack_alphabet, transitions=transitions, start_state='s', initial_stack_symbol='1', final_states={'q8'}, acceptance='final')
	return automata.read(tokens)