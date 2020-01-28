
class Doremi:

    def __init__(self):
        self.frequencies = []

    def addFrequency(self, data):
        self.frequencies.append(self.Frequency(data))

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
