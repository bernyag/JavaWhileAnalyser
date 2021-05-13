class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None


        

class Stack:    
    def __init__(self):
        self.head = Node('head')
        self.size = 0


    def __str__(self):
        element = self.head.next
        stack = []
        while element:
            stack.append(element.value)
            element = element.next
        return stack.__str__() 
    

    def getSize(self):
        return self.size
    

    def isEmpty(self):
        return self.size == 0
    

    def peek(self):
        ''' Devuelve el ultimo elemento agregado a la pila, sin eliminarlo. '''
        if self.isEmpty():
            raise Exception("Pila vacía; peek() no válido.")
        return self.head.next.value
    

    def push(self, value):
        ''' Agrega un elemento a la pila. '''
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
      

    def pop(self):
        ''' Devuelve el ultimo elemento, eliminandolo de la pila. '''
        if self.isEmpty():
            raise Exception("Pila vacía; pop() no válido.")
        element = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return element.value


    
    
class AutomataPila:
    def __init__(self, states, input_alphabet, stack_alphabet, transitions, start_state, initial_stack_symbol, final_states, acceptance='final'):
        self.__set_config__(states, input_alphabet, stack_alphabet, transitions, start_state, initial_stack_symbol, final_states, acceptance)


    def __clear_config__(self):
        self.states = set()
        self.input_alphabet = set()
        self.stack_alphabet = set()
        self.transitions = {}
        self.current_state = None
        self.stack = Stack()
        self.initial_stack_symbol = None
        self.final_states = set()
        self.acceptance = None


    def __verify_config__(self):
        ''' Verifica la validez del autómata. '''
        for state, path in self.transitions.items():
            if state not in self.states and state != '':
                raise Exception("El estado {} no es válido: {}.".format(state, self.states))
        if self.current_state not in self.states:
            raise Exception("El estado {} no es válido como estado de inicio.".format(self.current_state))
        if self.initial_stack_symbol not in self.stack_alphabet:
            raise Exception("El símbolo {} no es válido como inicio de la pila.".format(self.initial_stack_symbol))
        invalid_states = self.final_states - self.states
        if invalid_states:
            raise Exception("Estado(s) final(es) no válido(s): {}".format(', '.join(invalid_states)))
        if self.acceptance not in ('final', 'empty'):
            raise Exception("Aceptar por {} no es válido".format(self.acceptance))


    def __set_config__(self, states, input_alphabet, stack_alphabet, transitions, start_state, initial_stack_symbol, final_states, acceptance):
        self.__clear_config__()
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.current_state = start_state
        self.stack.push(initial_stack_symbol)
        self.initial_stack_symbol = self.stack.peek()
        self.final_states = final_states
        self.acceptance = acceptance
        self.__verify_config__()


    def read(self, tokens):
        tokens.append('')
        for token in tokens:
            self.__verify_input__(token)

            #print ("current state:", self.current_state)
            pop = self.stack.pop()

            if self.__lambda_transition__(self.transitions[self.current_state], pop):
                #print ("pop", pop)
                #print ("stack:", self.stack.__str__())
                self.current_state = self.transitions[self.current_state][''][pop][1]
                #print ("lambda transition to", self.current_state)
                #print()

            elif token in self.transitions[self.current_state]:
                #print ("reading token:", token)
                
                if pop in self.transitions[self.current_state][token]:
                    #print ("pop", pop)
                    
                    for elem in self.transitions[self.current_state][token][pop][0]:
                        #print ("push", elem)
                        self.stack.push(elem)
                        
                    #print ("stack:", self.stack.__str__())
                    self.current_state = self.transitions[self.current_state][token][pop][1]
                    #print ("transition to", self.current_state)
                    #print()
                    
                else: break
                    
            else: break

        if self.acceptance == 'final':
            if self.current_state in self.final_states:
                return True
            else: return False
        else:
            if self.stack.isEmpty():
                return True
            else: return False


    def __verify_input__(self, token):
        if token not in self.input_alphabet and token != '':
            raise Exception("{} no forma parte del alfabeto de entrada: {}.".format(token, self.input_alphabet))


    def __lambda_transition__(self, state, pop):
        if '' in state and pop in state['']:
            return True
        else: return False