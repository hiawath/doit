vowels=['a','e','i','o','u','1']
words = '''The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    nComplex is better than complicated.
    nFlat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"
'''
words=words.lower()
#found={'a':0,'e':0 ,'i':0,'o':0,'u':0,'1':0}
found={}


def printV3():
    for letter in words:
        if letter in vowels:
            found.setdefault(letter,0)
            found[letter] +=1

    for k,v in sorted(found.items()):
        print(k, ' : ', v)
    
def Test():
    pass
    
        