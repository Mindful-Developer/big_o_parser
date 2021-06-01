import re


class _ParseFunctionComplexity:
    def __init__(self, source):
        # class constants
        self.source = source.split("\n")

        # class variables
        self.function_name = ''
        self.parameters = []
        self.nested_functions = []
        self.big_o_lines = []
        self.annotated_source_code = []
        self.linked_variables = {}
        self.function_starting_indentation = []
        self.last_line_indentation_level = 0
        self.indentation_level = 0

        # start parse
        self.parse_function()

    def print_function(self):
        for line in self.annotated_source_code:
            print(line)

    def parse_function(self):
        for line in self.source:
            if line.find('#') != -1:
                line = line.split('#')[0]
            self.last_line_indentation_level = self.indentation_level
            self.indentation_level = self.check_indentation(line)
            if self.is_empty(line) or self.is_comment_or_decorator(line):
                self.annotated_source_code.append('')
                continue
            elif self.is_name_and_parameters(line) is not None:
                self.big_o_lines.append((0, len(line)))
                self.function_starting_indentation.append(self.check_indentation(line))
                self.annotated_source_code.append(line)
                continue
            else:
                self.annotated_source_code.append(line)

    def check_indentation(self, line):
        indentation_pattern = r'(^[ \t]*)'
        match = re.match(indentation_pattern, line)
        if match:
            return match.group(1).count(' ') + match.group(1).count('\t') * 4

    def is_name_and_parameters(self, line):
        func_and_params_pattern = r'^[ \t]*?def ([\w-]*)\(([\w\W, \n]*)\):'
        match = re.match(func_and_params_pattern, line)
        if match and not self.function_name:
            self.function_name = match.group(1)
            self.parameters = [x.strip() for x in match.group(2).split(',')]
        elif match:
            self.nested_functions.append([match.group(1), [x.strip() for x in match.group(2).split(',')]])
        else:
            return None
        return 0

    def is_list_comprehension(self, line):
        list_comprehension_pattern = r'\[(.*for.*in.*)]'
        match = re.match(list_comprehension_pattern, line)
        if match:
            return True

    def is_function(self, line):
        function_pattern = r'([^ ][\w\d]*)\(([\w\W]*?)\)'
        match = re.match(function_pattern, line)
        if match:
            return True

    def is_loop(self, line):
        for_loop_pattern = r'^[ \t]*?for ([\w\W]*) in ([\w\W]*):'
        while_loop_pattern = r'^[ \t]*?while ([\w\W]*):'
        match_1 = re.match(for_loop_pattern, line)
        match_2 = re.match(while_loop_pattern, line)
        if match_1 or match_2:
            return True

    def is_recursion(self, line):
        recursion_pattern = self.function_name + r'\(([\w\W, \n]*)\)'
        match = re.match(recursion_pattern, line)
        if match:
            return True

    def is_multiline(self, line):
        multiline_pattern = r'[,+\\][ ]*?$'
        match = re.match(multiline_pattern, line)
        if match:
            return True

    def is_method(self, line):
        pass

    @staticmethod
    def is_empty(line):
        empty_pattern = r'^[ \t]*$'
        match = re.match(empty_pattern, line)
        if not line or match:
            return True

    @staticmethod
    def is_comment_or_decorator(line):
        comment_pattern = r'^[ \t]*?[#@]'
        match = re.match(comment_pattern, line)
        if match:
            return True

    @staticmethod
    def get_o_single(complexity_number):
        complexity_dict = {
            0: 'O(1) - Constant',
            1: 'O(log(n)) - Logarithmic',
            2: 'O(sqrt(n)) - Square Root',
            3: 'O(n) - Linear',
            4: 'O(n log(n)) - Linearithmic',
            5: 'O(n^2) - Quadratic',
            6: 'O(n^3) - Cubic',
            7: 'O(2^n) - Exponential',
            8: 'O(n!) - Factorial'
        }
        return complexity_dict[complexity_number]
