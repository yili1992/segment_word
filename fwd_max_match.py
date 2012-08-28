#!/usr/bin/env python
#coding:utf8
'''
@author: andyHu
2012-8-27
'''
def u(s, encoding):
    if isinstance(s, unicode):
        return s
    return unicode(s, encoding)

def forword_max_match(words_dict, max_len, origin_str):
    '''forward max match segment'''
    words = []
    str_len = len(origin_str)
    while str_len > 0:
        if str_len > max_len:
            word_len = max_len
        else:
            word_len = str_len
        sub_str = origin_str[0:word_len]

        while word_len > 1:
            if sub_str in words_dict:
                break
            else:
                word_len = word_len - 1
                sub_str = sub_str[0:word_len]

        words.append(sub_str)
        origin_str = origin_str[word_len:]
        str_len = str_len - word_len
    return words

def _test():
    words = open('dict.dat')
    words_dict = {}
    max_value = -1
    for word in words:
        words_dict[u(word.strip(), 'utf-8')] = 1
        #获取最大向前匹配的长度, 即是字典中最长的单词的长度
        if len(word) > max_value:
            max_value = len(word)

    origin_str = ur'怎么说呢, 我觉得你是一个大笨蛋你说是不是'
    words = forword_max_match(words_dict, max_value, origin_str)

    for word in words:
        print word

if __name__ == '__main__':
    _test()
