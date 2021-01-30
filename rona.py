# © 2020 Seungheon Oh
# 'Ronacode interpreter implemented in python3

import sys
import re

STACK_SIZE = 1024


class Pandemics:
    def __init__(self):
        self.stack = [0] * STACK_SIZE
        self.pointer = 0
        self.order_record = []
        self.loop_match = 0
        self.order_stack = []

    def CurrentCases(self):
        return self.stack[self.pointer]

    def Corona(self, order):
        self.stack[self.pointer] += int((len(order) - 4) / 2)
        self.stack[self.pointer] %= 256

    def Mask(self, order):
        self.stack[self.pointer] -= int((len(order) - 4) / 2) + 1
        self.stack[self.pointer] %= 256

    def More(self, order):
        self.pointer += 1
        self.pointer %= STACK_SIZE

    def Less(self, order):
        self.pointer -= 1
        self.pointer %= STACK_SIZE

    def Isolate(self, order):
        self.order_stack.append([])

    def Expose(self, order):
        if len(self.order_stack) == 0:
            raise Exception('Attempt to expose without isolation')

        curr_loop_depth = len(self.order_stack)
        match = 0
        while self.CurrentCases() != 0:
            for o in self.order_stack[-1]:
                if len(self.order_stack) == curr_loop_depth or (o == 'expose' and match == 0):
                    self.do(o)(o)
                    continue
                if o == 'isolate':
                    match += 1
                elif o == 'expose':
                    match -= 1

                self.order_stack[-1].append(o)

        self.order_stack.pop()

    def Achoo(self, order):
        print(chr(self.CurrentCases()), end='')

    def Gasp(self, order):
        self.stack[self.pointer] = ord(input()[0])

    def noop(self, order):
        pass

    def do(self, order):
        VirusTests = {
            "co[ro]+na": self.Corona,
            "ma[as]*sk": self.Mask,
            "more": self.More,
            "less": self.Less,
            "isolate": self.Isolate,
            "expose": self.Expose,
            "achoo": self.Achoo,
            "gasp": self.Gasp,
        }
        for test, result in VirusTests.items():
            if re.match(test, order):
                return result
        return self.noop

    def AnalyzeVirus(self, order):
        if len(self.order_stack) == 0 or (order == 'expose' and self.loop_match == 0):
            return self.do(order)

        if order == 'isolate':
            self.loop_match += 1
        elif order == 'expose':
            self.loop_match -= 1

        self.order_stack[-1].append(order)
        return self.noop

    def ExecutiveOrder(self, order):
        self.AnalyzeVirus(order)(order)
        self.order_record.append(order)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('No input file')

    virus = open(sys.argv[len(sys.argv) - 1], 'r').read().replace('\n', ' ').split(" ")
    TheWorld = Pandemics()

    for order in virus:
        TheWorld.ExecutiveOrder(order)
