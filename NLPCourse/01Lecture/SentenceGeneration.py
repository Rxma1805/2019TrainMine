grammar = """
stmt = if block else block
block = cmp; assigment
assgiment = XXX
XXX
"""
decimal_grammar = """
expression = operator op operator
operator = num op num
num = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | num num
op = + | - | * | /
"""
grammar = """
sentence => noun_phrase verb_phrase 
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article =>  一个 | 这个
noun =>   女人 |  篮球 | 桌子 | 小猫
verb => 看着   |  坐在 |  听着 | 看见
Adj =>   蓝色的 |  好看的 | 小小的
"""
import random

def parse_grammar(grammer_str,sep='=>'):
    grammer={}
    for line in grammer_str.split('\n'):
        line = line.strip()
        if not line : continue
        target,rules = line.split(sep)
        grammer[target.strip()] = [rule.strip() for rule in rules.split('|') ]
    return  grammer


def gene(grammer_parsed,targent='sentence'):
    if targent not in grammer_parsed:
        return targent
    rules = random.choice(grammer_parsed[targent])
    return ''.join(gene(grammer_parsed,r.strip()) for r in rules.split(' ') if r != 'null')

g = parse_grammar(grammar,sep='=>')
for _ in range(20):
    print(gene(g,'sentence'))

g = parse_grammar(decimal_grammar, sep='=')
for _ in range(20):
    print(gene(g, 'expression'))