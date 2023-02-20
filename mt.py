import sys
import json

if len(sys.argv) < 2:
    print("Usar: python ./mt.py [MT] [Word]")
    sys.exit()

json_mt = json.load(open(sys.argv[1]))

alfa_entry = json_mt['mt'][1] # alfabeto de entrada, cujo esta contido no alfabeto da fita
ini_state  = json_mt['mt'][6] # estado inicial
states     = json_mt['mt'][0] # estados
tape_spec  = json_mt['mt'][2]

#[marcador inicio, simbolo vazio, alfabeto de entrada simbol, ...,
# alfabeto da fita simbol, ...]

ini_simbol   = json_mt['mt'][3] #marcador inicio
empty_simbol = json_mt['mt'][4] #simbolo vazio
transitions  = json_mt['mt'][5] #transicoes

# json_mt['mt'][5][n] transicao [e1, a, e2, b, d]

finals_states = json_mt['mt'][7] #estados finais

if len(sys.argv) < 3:
    word = ''
else:
    word = [_ for _ in sys.argv[2]]

state = ini_state

if len(list((set(word).difference(set(alfa_entry))))) > 0:
    print("Não")
    sys.exit()

if word != '':
    tape = [ini_simbol] + word + [empty_simbol]*10
else:
    tape = [ini_simbol] + [''] + [empty_simbol]*10
    

index = 1
head = tape[index]

while ([state, head] in [_[:2] for _ in transitions]):
    transindex = [_[:2] for _ in transitions].index([state, head])
    transition = transitions[transindex]

    if transition[3] not in tape_spec:
        print("Não")
        sys.exit()
    tape[index] = transition[3]
    if transition[4]=='>':
        index += 1
        tape.append(empty_simbol) # virtual infinit list
    elif transition[4]=='<':
        index -= 1
    state = transition[2]
    head = tape[index]

if state not in finals_states:
    print("Não")
else:
    print("Sim")