num_exps = 30
max_indvs = 300
max_len_cromo = 100000
max_instr = 70
len_nombre_tret = 30

import random
import string
from bintree import BinTree

def generate_binary_tree(n):
    assert n % 2 == 1, "n must be odd"

    val = list(range(1, n + 1))
    random.shuffle(val)

    def helper(v):
        if len(v) == 1:
            return BinTree(v[0], BinTree(0), BinTree(0))
        else:
            a = (len(v) - 2)//2
            m = random.randint(0, a)*2 + 1
            l = helper(v[1:m + 1])
            r = helper(v[m + 1:])
            return BinTree(v[0], l, r)
    
    return helper(val)

comandos = ["consulta_individu", "distribucio_tret", "consulta_tret", "afegir_tret"]
trets = set()

for i in range(num_exps):

    n = random.randint(2, max_indvs)
    if n % 2 == 0:
        n -= 1

    m = random.randint(1, max_len_cromo)
    print(f"experiment {n} {m}")

    t = generate_binary_tree(n)
    print(' '.join(map(str, t.preorder())))

    for j in range(n):
        print(''.join(random.choices(["0", "1"], k = 2*m)))

    for j in range(random.randint(1, max_instr)):
        com = random.choices(comandos, weights=[1, 1, 1, 3], k = 1)[0]
        if com == "consulta_individu":
            print(f"{com} {random.randint(1, n)}")
        elif com == "afegir_tret":
            if len(trets) != 0:
                contiene = random.randint(0, 1)
                if contiene:
                    ran = random.sample(sorted(trets), 1)[0]
                else:
                    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = len_nombre_tret))
            else:
                ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = len_nombre_tret))
            trets.add(ran)
            print(f"{com} {ran} {random.randint(1, n)}")
        elif com == "distribucio_tret":
            if len(trets) != 0:
                contiene = random.randint(0, 1)
                if contiene:
                    ran = random.sample(sorted(trets), 1)[0]
                else:
                    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = len_nombre_tret))
            else:
                ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = len_nombre_tret))
            print(f"{com} {ran}")
        elif com == "consulta_tret":
            if len(trets) != 0:
                contiene = random.randint(0, 1)
                if contiene:
                    ran = random.sample(sorted(trets), 1)[0]
                else:
                    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = len_nombre_tret))
            else:
                ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = len_nombre_tret))
            print(f"{com} {ran}")

print("fi")