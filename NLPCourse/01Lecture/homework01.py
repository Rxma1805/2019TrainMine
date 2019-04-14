def is_variable(pat):
    return pat.startswith('?') and all(s.isalpha() for s in pat[1:])

def is_pattern_segment(pat):
    return pat.startswith('?*') and all(s.isalpha() for s in pat[2:])

fail = [ False]
def pat_match(pattern, saying):
    if not pattern or not saying: return []
    pat = pattern[0]
    if is_variable(pat):
        return [(pat, saying[0])] + pat_match(pattern[1:], saying[1:])
    elif is_pattern_segment(pat):
        match, index = segment_match(pattern, saying)
        return [match] + pat_match(pattern[1:], saying[index:])
    elif pat == saying[0]:
        return pat_match(pattern[1:], saying[1:])
    else:
        return fail

def segment_match(pattern,saying):
    seg_pat,seg_rest = pattern[0],pattern[1:]
    seg_pat = seg_pat.replace('?*','?')
    if not seg_rest:return (seg_pat,saying),len(saying)
    for k,v in enumerate(saying):
        if seg_rest[0] == v:
            return  (seg_pat,saying[:k]),k
    return (seg_pat,saying),len(saying)

def pat_to_dic(pattern):
    return {k: ' '.join(v) if isinstance(v,list) else v for k,v in pattern}

def subsitite(rule,parsed_rule_dic):
    if not rule:return []
    return [parsed_rule_dic.get(rule[0],rule[0])]+ subsitite(rule[1:],parsed_rule_dic)

defined_patterns = \
    {
        "I need ?X": ["Image you will get ?X soon", "Why do you need ?X ?"],
        "My ?X told me something": ["Talk about more about your ?X", "How do you think about your ?X ?"],
        '?*x hello ?*y': ['How do you do', 'Please state your problem'],
        '?*x I want ?*y': ['what would it mean if you got ?y', 'Why do you want ?y', 'Suppose you got ?y soon'],
        '?*x if ?*y': ['Do you really think its likely that ?y', 'Do you wish that ?y', 'What do you think about ?y', 'Really-- if ?y'],
        '?*x no ?*y': ['why not?', 'You are being a negative', 'Are you saying \'No\' just to be negative?'],
        '?*x I was ?*y': ['Were you really', 'Perhaps I already knew you were ?y', 'Why do you tell me you were ?y now?'],
        '?*x I feel ?*y': ['Do you often feel ?y ?', 'What other feelings do you have?']
    }

def count_variable_nums(rules):
    print (rules.count('?'))

import random
def get_response(saying,rules=defined_patterns):
    for k in rules.keys():
        pattern = pat_match(k.split(), saying.split())
        if False not in pattern and len(pattern[0][1]) != len(saying.split()) :
            # print("parameter :"+k)
            # print("pattern_dic")
            # #print(pattern)
            # print(pat_to_dic(pattern))
            # if len(pat_to_dic(pattern)) != count_variable_nums(k):
            #     continue
            response = random.choice(rules[k])
            # print(response)
            return ' '.join(subsitite(response.split(), pat_to_dic(pattern)))

    return ""

sentence = ["I need MacBook","My Brother told me something",
            'OK,that fun. hello my smart daughter','i had told you I want buy a macbook',
            'what is going  if i did not do my homework', 'please say no when someone bother you',
            'i am really sorry, I was an honest boy','the noodle, I feel just so so']
for _ in range(20):
    one = random.choice(sentence)
    print('*******')
    print(one)
    print(get_response(one))