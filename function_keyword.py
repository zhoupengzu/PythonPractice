# coding=utf-8
def key_word(name,age,**keyword):
    print name,age,keyword;
    return;
key_word("name1","10");
key_word("name2","20",city="beijing");
key_word("name3","30",city="beijing",job="engineer");

kw = {"city":"beijing","job":"engineer"};
key_word("name4","40",**kw);