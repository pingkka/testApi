import urllib.request
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor
from soynlp.tokenizer import MaxScoreTokenizer
from soynlp.tokenizer import LTokenizer
# -*- coding: utf-8 -*-
from ckonlpy.tag import Twitter

from pykospacing import spacing

#띄어 쓰기 자동으로 해줌
sent = "위 인수들을 사용할 때 고려해야 될점이있습니다. audio 데이터의 어떤 시점에 하나의 단어가 언급되고 있다면 그 단어는 잘려서 이상하게 인식될 것입니다. 이 harvard 데이터는 실험 목적으로 녹음된 것이기 때문에 초 단위로 잘라도 단어가 잘리지 않은 것 입니다."
new_sent = sent.replace(" ", '')
print(new_sent)
kospacing_sent = spacing(new_sent)
print(sent)
print(kospacing_sent)

#특정 단어 명사로 설정
twitter = Twitter()
#twitter.add_dictionary('띄어쓰기', 'Noun')
print(twitter.morphs(kospacing_sent))

