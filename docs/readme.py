import os
import sys

def walk(file):
    for root, dirs, files in os.walk(file):
        for f in files:
            yield os.path.join(root, f)

        for d in dirs:
            walk(os.path.join(root, d))

items = []
for f in walk('.'):
    if f.endswith('.txt'):
        os.remove(f)
        # with open(f.replace('.txt','.md'),'wt',encoding='utf-8') as fw:
        #     with open(f,'rt',encoding='mbcs') as fr:
        #         fw.writelines(fr.readlines())
        # filePath = os.path.splitext(f)[0].replace('.','').replace('\\','//')
        # fileName = filePath.split('//')[-1]
        # print(f'[{fileName}](#docs/{filePath})')
        