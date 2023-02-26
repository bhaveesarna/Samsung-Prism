class parser:
    def __init__(self,file_name) -> None:
        self.DATATYPE = ['int', 'float', 'char', 'string', 'bool','void']
        self.DATATYPE += list(map(lambda x: x+'*',self.DATATYPE))
        self.file = file_name
        self.funcs = []
    
    def get_func_lines(self) -> None:
        f = open(self.file,'r+')
        lines = [line.strip() for line in f.readlines()]
        lines = [line for line in lines if not line.startswith("//") and len(line) > 0]
        for i in range(len(lines)):
            if lines[i].startswith("const"):
                lines[i] = lines[i][6:]
        defs = [line for line in lines if line.split()[0] in self.DATATYPE]
        funcs = []
        for d in defs:
            if '(' in d.split()[1]:
                self.funcs.append(d)

    def get_functions(self):
        self.get_func_lines()
        function_objs = []
        for func in self.funcs:
            content = self.get_function_content(func)
            ret =  func.split()[0]
            func = func[len(ret):]
            name = func.split('(')[0]
            func =func[len(name):]
            args = func[1:func.find(')')]
            argnames = list(filter(lambda x: x not in self.DATATYPE and x != "const", args.split()))
            argtypes = list(filter(lambda x: x in self.DATATYPE and x != "const", args.split()))
            f = function(name,argtypes,argnames,content,ret)
            function_objs.append(f)
        return function_objs
            

    def get_function_content(self,func):
        f = open(self.file,'r+')
        lines = [line.strip() for line in f.readlines()]
        lines = [line for line in lines if not line.startswith("//") and len(line) > 0]
        codestr = " ".join(lines)
        idx = codestr.find(func) + len(func)
        stack = ['{']
        content = ''
        while idx < len(codestr):
            if codestr[idx] == '{':
                stack.append('{')
            if codestr[idx] == '}':
                stack.pop()
            if len(stack) == 0:
                break
            content += codestr[idx]
            idx += 1
        return content

class function:
    def __init__(self,name,argtypes,argnames,content,ret) -> None:
        self.name = name
        self.args = {}
        self.content = content
        self.ret = ret

        for i in range(len(argnames)):
            if argtypes[i] in self.args:
                self.args[argtypes[i]].append([argnames[i]])            
            else:
                self.args[argtypes[i]] = [argnames[i]]

    def head_serialize(self):
        s = f'{self.ret} {self.name}('
        for k in self.args:
            if len(self.args[k]) > 1:
                for v in self.args[k]:
                    s += k + ' ' + v + ', '
            else:
                s += k + ' ' + self.args[k][0] + ', '
        s = s[:-2]
        s += ')'
        return s

    def generate_bind_text(self, filename):
        bind_text = f'PYBIND11_MODULE({filename}, m){{\nm.def(\"{self.name}\",&{self.name})\n}}'
        return bind_text

    

