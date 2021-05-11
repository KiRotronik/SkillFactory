with open('input.txt', 'w', encoding = 'utf8') as inp:
    inp.write('333333\n')
    inp.write('333333433\n')
    inp.write('331113333\n')

with open('input.txt', 'r', encoding='utf8') as inp:
    with open('output.txt', 'w', encoding = 'utf8') as outp:
        for i in inp:
            outp.write(i)

with open('numbers.txt', 'r', encoding='utf8') as n:
    with open('output.txt', 'a', encoding='utf8') as outp:
        min_ = max_ = int(n.readline())
        for i in n:
            if int(i) < min_:
                min_ = int(i)
            elif int(i) > max_:
                max_ = int(i)
        outp.write(str(min_ + max_))

with open('name.txt', 'r') as na:
    for i in na:
        if int(i.split()[-1]) <= 3:
            print(na)
