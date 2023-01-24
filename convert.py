import os
import json

prompt_dir = "prompts/"
src_dir = "completion/"

def open_file(filePath):
    with open(filePath,'r', encoding='utf-8') as infile:
        return infile.read()

if __name__ == '__main__':
    files = os.listdir(src_dir)
    data = list()
    for file in files:
        completion = open_file (src_dir + file)
        prompt = open_file (prompt_dir + file)
        info = {'prompt': prompt, 'completion': completion}
        data.append(info)
    with open ('sop.jsonl', 'w') as outfile:
        for i in data:
            json.dump (i, outfile)
            outfile.write('\n')
