defined_patterns = \
    {
        '?*x我想?*y': ['你觉得?y有什么意义呢？', '为什么你想?y', '你可以想想你很快就可以?y了'],
        '?*x我想要?*y': ['?x想问你，你觉得?y有什么意义呢?', '为什么你想?y', '?x觉得... 你可以想想你很快就可以有?y了', '你看?x像?y不', '我看你就像?y'],
        '?*x喜欢?*y': ['喜欢?y的哪里？', '?y有什么好的呢？', '你想要?y吗？'],
        '?*x讨厌?*y': ['?y怎么会那么讨厌呢?', '讨厌?y的哪里？', '?y有什么不好呢？', '你不想要?y吗？'],
        '?*x机器人?*y': ['你为什么要提机器人的事情？', '你为什么觉得机器人要解决你的问题？'],
        '?*x对不起?*y': ['不用道歉', '你为什么觉得你需要道歉呢?'],
        '?*x我记得?*y': ['你经常会想起这个吗？', '除了?y你还会想起什么吗？', '你为什么和我提起?y'],
        '?*x如果?*y': ['你真的觉得?y会发生吗？', '你希望?y吗?', '真的吗？如果?y的话', '关于?y你怎么想？'],
        '?*x我?*z梦见?*y':['真的吗? --- ?y', '你在醒着的时候，以前想象过?y吗？', '你以前梦见过?y吗'],
        '?*x妈妈?*y': ['你家里除了?y还有谁?', '嗯嗯，多说一点和你家里有关系的', '她对你影响很大吗？'],
        '?*x爸爸?*y': ['你家里除了?y还有谁?', '嗯嗯，多说一点和你家里有关系的', '他对你影响很大吗？', '每当你想起你爸爸的时候， 你还会想起其他的吗?'],
        '?*x我愿意?*y': ['我可以帮你?y吗？', '你可以解释一下，为什么想?y'],
        '?*x我很难过，因为?*y': ['我听到你这么说， 也很难过', '?y不应该让你这么难过的'],
        '?*x难过?*y': ['我听到你这么说， 也很难过',
                     '不应该让你这么难过的，你觉得你拥有什么，就会不难过?',
                     '你觉得事情变成什么样，你就不难过了?'],
        '?*x就像?*y': ['你觉得?x和?y有什么相似性？', '?x和?y真的有关系吗？', '怎么说？'],
        '?*x和?*y都?*z': ['你觉得?z有什么问题吗?', '?z会对你有什么影响呢?'],
        '?*x和?*y一样?*z': ['你觉得?z有什么问题吗?', '?z会对你有什么影响呢?'],
        '?*x我是?*y': ['真的吗？', '?x想告诉你，或许我早就知道你是?y', '你为什么现在才告诉我你是?y'],
        '?*x我是?*y吗': ['如果你是?y会怎么样呢？', '你觉得你是?y吗', '如果你是?y，那一位着什么?'],
        '?*x你是?*y吗':  ['你为什么会对我是不是?y感兴趣?', '那你希望我是?y吗', '你要是喜欢， 我就会是?y'],
        '?*x你是?*y' : ['为什么你觉得我是?y'],
        '?*x因为?*y' : ['?y是真正的原因吗？', '你觉得会有其他原因吗?'],
        '?*x我不能?*y': ['你或许现在就能?*y', '如果你能?*y,会怎样呢？'],
        '?*x我觉得?*y': ['你经常这样感觉吗？', '除了到这个，你还有什么其他的感觉吗？'],
        '?*x我?*y你?*z': ['其实很有可能我们互相?y'],
        '?*x你为什么不?*y': ['你自己为什么不?y', '你觉得我不会?y', '等我心情好了，我就?y'],
        '?*x好的?*y': ['好的', '你是一个很正能量的人'],
        '?*x嗯嗯?*y': ['好的', '你是一个很正能量的人'],
        '?*x不嘛?*y': ['为什么不？', '你有一点负能量', '你说 不，是想表达不想的意思吗？'],
        '?*x不要?*y': ['为什么不？', '你有一点负能量', '你说 不，是想表达不想的意思吗？'],
        '?*x有些人?*y': ['具体是哪些人呢?'],
        '?*x有的人?*y': ['具体是哪些人呢?'],
        '?*x某些人?*y': ['具体是哪些人呢?'],
        '?*x每个人?*y': ['我确定不是人人都是', '你能想到一点特殊情况吗？', '例如谁？', '你看到的其实只是一小部分人'],
        '?*x所有人?*y': ['我确定不是人人都是', '你能想到一点特殊情况吗？', '例如谁？', '你看到的其实只是一小部分人'],
        '?*x总是?*y': ['你能想到一些其他情况吗?', '例如什么时候?', '你具体是说哪一次？', '真的---总是吗？'],
        '?*x一直?*y': ['你能想到一些其他情况吗?', '例如什么时候?', '你具体是说哪一次？', '真的---总是吗？'],
        '?*x或许?*y': ['你看起来不太确定'],
        '?*x可能?*y': ['你看起来不太确定'],
        '?*x他们是?*y吗？': ['你觉得他们可能不是?y？']
    }

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
        if len(saying) == index and pattern[1:]:
            return fail
        else:
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

import jieba
def my_split(words):
    seg_list=[]
    tmp=""
    for word in list(jieba.cut(words)):
        if word == '?':
            tmp = word
            continue
        elif word == '*' or word == 'x' or word == 'y' :
            tmp += word
            continue
        else:
            if tmp != "":
                seg_list.append(tmp)
                tmp=""
            seg_list.append(word)
    if tmp != "":
        seg_list.append(tmp)
    #print(seg_list)
    return seg_list





import random
import jieba


def get_response(saying,rules=defined_patterns):
    for k in rules.keys():
        pattern = pat_match(my_split(k),my_split(saying))
        if False not in pattern :
        # if False not in pattern and len(pattern[0][1]) != len(my_split(saying)) :
        #     print("parameter :"+k)
        #     print("pattern_dic")
        #     print(pat_to_dic(pattern))
            response = random.choice(rules[k])
            return ''.join(subsitite(my_split(response), pat_to_dic(pattern)))
    return ""

sentence=\
    [
        "妈妈，我想睡觉",
        "爸爸，我想要玩具",
        "我喜欢上学",
        "我讨厌吃菜",
        "什么是AI呀",
        "天猫精灵是一个机器人吗",
        "难道是我对不起你吗？",
        "老师，我记得昨天没有作业",
        "当初如果没有贪玩就好了",
        "昨天晚上我梦见钥匙丢了",
        "我爱妈妈做的菜",
        "我喜欢爸爸总是带我去玩",
        "明天我愿意来上这节课",
        "老师，我很难过，因为这道题我做不出来",
        "妈妈难过的时候让我不知所措"

    ]


# for _ in range(20):
#     one = random.choice(sentence)
#     print(one)
#     print(get_response(one))
#     print('------------')

#print(get_response("什么是AI呀"))
print(list(jieba.cut_for_search("?*xAI?*p")))