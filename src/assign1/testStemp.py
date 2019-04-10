#porter 스테밍 패키지
from stemming.porter2 import stem

list = ['automate', 'automated', 'automates', 'automating', 'automation', 'operate', 'operating', 'operates', 'operation', 'operative', 'operatives', 'operational']

print('porter stemming')
for i in list:
    print(i + ' : ' +  stem(i))
