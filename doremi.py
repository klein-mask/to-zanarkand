
class Doremi:

    def __init__(self):
        self.frequencies = []
        self.A0 = 0
        self.A1 = 1
        self.A2 = 2
        self.A3 = 3
        self.A4 = 4
        self.A5 = 5
        self.A6 = 6
        self.A7 = 7
        self.A8 = 8
        self.A9 = 9

    def addFrequency(self, data):
        self.frequencies.append(self.Frequency(data))

    def freq(self, key, doremi_str):
        print(doremi_str)
        return self.frequencies[key].get(doremi_str)

    class Frequency:
        def __init__(self, data):
            self.C = data[0]  # ド
            self.C1 = data[1]  # ド#
            self.D = data[2]  # レ
            self.D1 = data[3]  # レ#
            self.E = data[4]  # ミ
            self.F = data[5]  # ファ
            self.F1 = data[6]  # ファ#
            self.G = data[7]  # ソ
            self.G1 = data[8]  # ソ#
            self.A = data[9]  # ラ
            self.A1 = data[10]  # ラ#
            self.B = data[11]  # シ

        def get(self, s):
            if s == 'ド':
                return self.C
            elif s == 'ド+' or s == 'レ-':
                return self.C1
            elif s == 'レ':
                return self.D
            elif s == 'レ+' or s == 'ミ-':
                return self.D
            elif s == 'ミ':
                return self.E
            elif s == 'ファ':
                return self.F
            elif s == 'ファ+' or s == 'ソ-':
                return self.F1
            elif s == 'ソ':
                return self.G
            elif s == 'ソ+' or s == 'ラ-':
                return self.G1
            elif s == 'ラ':
                return self.A
            elif s == 'ラ+' or s == 'シ-':
                return self.A1
            elif s == 'シ':
                return self.B
