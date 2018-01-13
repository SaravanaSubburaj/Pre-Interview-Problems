import json
from pprint import pprint

alma = {}

def text_parser(q):
    if 'text' in q:
        if not 'options' in q:
            q['options'] = ''
        alma[q['var']] = input(q['text'] + ' ' + ' | '.join(q['options']) + ' : ')


def instruction_parser(q):
    if not 'instruction_var' in q:
        return q['instruction']
    else:
        return q['instruction'] % tuple(alma[x] for x in q['instruction_var'])

def calculation_parser(q):
    global alma
    if q['calculated_variable'] == 'True':
        alma[q['var']] = eval(q['formula'])


with open('assignment_1_input_2.json',encoding='utf-8',mode='r') as f1:
    data = json.load(f1)

questions = data['questions']

for ques in questions:

    locals().update(alma)
    if 'instruction' in ques:
        print(instruction_parser(ques))

    elif 'conditions' in ques:
        for condition in ques['conditions']:
            while not all(list(map(eval,condition))):
                text_parser(ques)
                locals().update(alma)

    elif 'calculated_variable' in ques:
        calculation_parser(ques)
        continue

    else:
        text_parser(ques)




