class Garden:
    def __init__(self, diagram,
                 students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self._diagram = diagram.split("\n")
        self._students = sorted(students)
        self._palnts_names = {
            "G": "Grass",
            "V": "Violets",
            "R": "Radishes",
            "C": "Clover"
        }

    def plants(self, student):
        index = self._students.index(student) * 2
        plants_prefix = "".join(row[index:index + 2] for row in self._diagram)
        return [self._palnts_names[plant] for plant in plants_prefix]
        