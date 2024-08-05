class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        import collections
        
        def parse_formula(formula):
            n = len(formula)
            i = 0
            stack = [collections.Counter()]
            
            while i < n:
                if formula[i] == '(':
                    stack.append(collections.Counter())
                    i += 1
                elif formula[i] == ')':
                    i += 1
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplier = int(formula[i_start:i] or 1)
                    top = stack.pop()
                    for elem, count in top.items():
                        stack[-1][elem] += count * multiplier
                else:
                    i_start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    elem = formula[i_start:i]
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[i_start:i] or 1)
                    stack[-1][elem] += count
            
            return stack.pop()
        
        counter = parse_formula(formula)
        elements = sorted(counter.keys())
        
        result = []
        for elem in elements:
            result.append(elem)
            if counter[elem] > 1:
                result.append(str(counter[elem]))
        
        return ''.join(result)