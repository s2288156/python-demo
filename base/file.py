import csv
import os

stPath = os.path.join('d:\\', "st.txt")
st = open(stPath, 'w')
st.write("Hello world")
st.close()

with open(stPath, 'w') as f:
    print(f.write("Hi"))

with (open('d:\\text.csv', 'w') as f):
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Name', 'Age', 'Level'])
    writer.writerow(['Lao Wang', '30', 'P8'])
    writer.writerow(['Li Si', '38', 'P9'])
