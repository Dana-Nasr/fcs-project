class User:
    def __init__(self, id, name, subjects, topics):  ##list subject dict topics
        self.id = id
        self.name = name
        self.subjects = subjects
        self.topics = topics

    def addSubject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

    