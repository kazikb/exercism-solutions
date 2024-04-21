class Scale:

    CHROMATIC_SCALE_SHARP = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")
    CHROMATIC_SCALE_FLAT = ("A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab")
    FLATS = ('F','Bb','Eb','Ab','Db','Gb','d','g','c','f','bb','eb')
    INTERVAL = {'m': 1, 'M': 2, 'A': 3}

    def __init__(self, tonic):
        if tonic in self.FLATS: self.scale = self.CHROMATIC_SCALE_FLAT
        else: self.scale = self.CHROMATIC_SCALE_SHARP
        self.tonic = tonic.capitalize()

    def chromatic(self):
        index = self.scale.index(self.tonic)
        return [self.scale[(i + index) % 12] for i in range(12)]

    def interval(self, intervals):
        result = [self.tonic]
        index = self.scale.index(self.tonic)
        for interval in intervals:
            index = (index + self.INTERVAL[interval]) % 12
            result.append(self.scale[index])
        return result
