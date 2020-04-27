from workWithXML import downloadFromXML, saveInXml

class Point:

    def __init__(self, kor=[0., 0., 0.], speed=[0., 0., 0.]):
        self.kor = kor
        self.speed = speed

    def strKor(self):
        return "x = " + str(self.kor[0]) + "\ny = " + str(self.kor[1]) + "\nz = " + str(self.kor[2])

    def strSpeed(self):
        return "Vx = " + str(self.speed[0]) + "\nVy = " + str(self.speed[1]) + "\nVz = " + str(self.speed[2])

    def action(self, t, F):
        for i in range(3):
            self.kor[i] = self.kor[i] + self.speed[i] * t + (F[i] * (t ** 2)) / 2
            self.speed[i] = self.speed[i] + F[i] * t

    def download(self):
        self.kor, self.speed = downloadFromXML()

    def save(self):
        saveInXml(self.kor, self.speed)
