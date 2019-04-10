from konlpy.tag import Okt

s = u'뭄바이에서 발생한 테러와 관련하여 한국대사관에서는 한국인들의 사망과 부상 피해를 조사하고 있다.'
okt = Okt()

print(okt.nouns(s))
