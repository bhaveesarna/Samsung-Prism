class Test:
    def __init__(self,test_name,test_suite_name) -> None:
        self.test_name = test_name
        self.test_suite_name = test_suite_name
        self.assertions = []
    
    def add_assertion(self,assertion_type,params) -> None:
        self.assertions.append(assertion(assertion_type,params))

    def serialize_assertions(self) -> str:
        st = ''
        for assertion in self.assertions:
            st += assertion.serialize()
            st += ';'
            st += '\n'
        return st


    def serialize(self) -> None:
        return f'TEST({self.test_name}, {self.test_suite_name}){{\n{self.serialize_assertions()}}}'

class assertion:
    def __init__(self,assertion_type,params) -> None:
        self.type = assertion_type
        self.params = params
    
    def serialize(self) -> str:
        param_string = ''
        for param in self.params:
            param_string += param
            param_string += ', '
        param_string = param_string[:-2]
        return f'{self.type}({param_string})'