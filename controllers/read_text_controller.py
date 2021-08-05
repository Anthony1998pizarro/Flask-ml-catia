import re
def readTxt(text):
  f = open (text,'r',encoding='UTF-8')
  data = []
  for i in f.readlines():
    data.append(re.sub('[^A-Za-záéíóúñ]+',' ',i.strip('\n')))
  f.close()
  return data