import os

def read(file):
    with open(file, 'r', encoding='utf-8') as infile:
        return infile.read()


def save(content, file):
    with open('prompts/%s' % file, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


files = os.listdir('Student-info/')
for file in files:
    content = read('Student-info/' + file)
    prompt = read('prompt.txt').replace('<<STUDENT_INFO>>', content)
    save(prompt, file)
