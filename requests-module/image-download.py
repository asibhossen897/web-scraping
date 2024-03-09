import requests
import sys

img_url = sys.argv[1]
file_name = sys.argv[2]
r = requests.get(img_url)

with open(file_name, 'wb') as f:
  f.write(r.content)

# a = 10
# b = 5
# print(a+b)

# import sys

# print(sys.argv)
# print(type(sys.argv))

# arguments = sys.argv

# a = arguments[1]
# b = arguments[2]

# print(int(a)+int(b))