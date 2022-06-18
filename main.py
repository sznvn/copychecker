import exctractor
#
import processor
from configuration import path

text = exctractor.extract(path)

f = processor.format(text)

print(f)
print(text[207:222], text[362:373])




if __name__ == '__main__':
    print('PyCharm')

