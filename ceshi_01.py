from pypinyin import  pinyin,lazy_pinyin
def get_stroke(c):
  # 如果返回 0, 则也是在unicode中不存在kTotalStrokes字段
  strokes = []
  strokes_path = '/Users/dongxu.zhao1/githome/baby-names/docs/strokes.txt'
  with open(strokes_path, 'r') as fr:
    for line in fr:
      strokes.append(int(line.strip()))

  unicode_ = ord(c)

  if 13312 <= unicode_ <= 64045:
    return strokes[unicode_-13312]
  elif 131072 <= unicode_ <= 194998:
    return strokes[unicode_-80338]
  else:
    print("c should be a CJK char, or not have stroke in unihan data.")
    # can also return 0

char = "凡磊"

def get_pinyin(char):
  _pinyin_list = pinyin(char)
  _pinyin = ''
  for i in range(len(char)):
    _pinyin += _pinyin_list[i][0]
  return _pinyin



s = get_pinyin(char)
total = 0
for s in char:
  total += get_stroke(s)
print(total)
import re
ss = "名字‘金登’全国同名同姓人数为47人，其中男性人数为44人，女性人数为3人"
total_re = r"全国同名同姓人数为([0-9]{0,})人"
boy_re = r"其中男性人数为([0-9]{0,})人"
girl_re = r"女性人数为([0-9]{0,})人"

match = re.search(total_re, ss)
print(match.group(1))
match = re.search(boy_re, ss)
print(match.group(1))
match = re.search(girl_re, ss)
print(match.group(1))