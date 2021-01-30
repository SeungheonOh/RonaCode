import sys
import re

STACK_SIZE = 15

class Pandemics:
    def __init__(self):
        self.stack = [0] * STACK_SIZE
        self.pointer = 0
        self.order_record = []
        self.isolations = []

    def CurrentCases(self):
        return self.stack[self.pointer]

    def Corona(self, order):
        self.stack[self.pointer] += int((len(order) - 4) / 2)
        self.stack[self.pointer] %= 256

    def Mask(self, order):
        self.stack[self.pointer] -= int((len(order) - 4) / 2) + 1
        self.stack[self.pointer] %= 256

    def More(self, order):
        self.pointer += 1;
        self.pointer %= STACK_SIZE

    def Less(self, order):
        self.pointer -= 1;
        self.pointer %= STACK_SIZE

    def Isolate(self, order):
        self.isolations.append(len(self.order_record))
        pass

    def Expose(self, order):
        isol = self.isolations.pop()
        for i, order in enumerate(self.order_record[isol + 1:]):
            print(order)
        pass

    def Achoo(self, order):
        print(chr(self.CurrentCases()))

    def Gasp(self, order):
        pass

    def noop(self, order):
        pass

    def AnalyzeVirus(self, order):
        VirusTests = {
                "co[ro]+na": self.Corona,
                "ma[as]*sk": self.Mask,
                "more":       self.More,
                "less":      self.Less,
                "isolate":   self.Isolate,
                "expose":    self.Expose,
                "achoo":     self.Achoo,
                "gasp":      self.Gasp,
        }
        for test, result in VirusTests.items():
            if re.match(test, order):
                return result
        return self.noop

    def ExecutiveOrder(self, order):
        self.AnalyzeVirus(order)(order)
        self.order_record.append(order)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('No input file')

    virus = open(sys.argv[len(sys.argv) - 1], 'r').read().replace('\n', '').split(" ")
    TheWorld = Pandemics()

    for order in virus:
        TheWorld.ExecutiveOrder(order)
        print('stack {}'.format(TheWorld.stack))
