class User:
    def __init__(self, id, name, subjects, topics):  ##list subject dict topics
        self.id = id
        self.name = name
        self.subjects = subjects
        self.topics = topics

    def addSubject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

    def addInterestedTopic(self, topic):                ##key 1 in dict
        if 'interested_in_topics' not in self.topics:
            self.topics['interested_in_topics'] = []
        if topic not in self.topics['interested_in_topics']:
            self.topics['interested_in_topics'].append(topic)


    def addKnowntTopic(self, topic):                    ##key 2 in dict
        if 'already_known_topics' not in self.topics:
            self.topics['already_known_topics'] = []
        if topic not in self.topics['already_known_topics']:
            self.topics['already_known_topics'].append(topic)   
    def printUser():
        print("id={self.id}, name={self.name}, subjects={self.subjects}, topics={self.topics}")


        