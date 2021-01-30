import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('No input file')

    bf = list(open(sys.argv[len(sys.argv) - 1], 'r').read().replace('\n', ''))

    rona = ''

    pluscnt = 0
    minuscnt = 0
    for cmd in bf:
        if cmd != '+' and pluscnt != 0:
            rona += "co" + ( "ro" * pluscnt ) + "na "
            pluscnt = 0

        if cmd != '-' and minuscnt != 0:
            rona += "m" + ( "as" * minuscnt ) + "k "
            minuscnt = 0


        if cmd == '+':
            pluscnt += 1
            continue
        elif cmd == '-':
            minuscnt += 1
            continue
        elif cmd == '>':
            rona += "more "
        elif cmd == '<':
            rona += "less "
        elif cmd == '[':
            rona += "isolate "
        elif cmd == ']':
            rona += "expose "
        elif cmd == ',':
            rona += "gasp "
        elif cmd == '.':
            rona += "achoo "
    print()
    print(rona)
