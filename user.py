class User:
    def __init__(self, id, name, subjects, topics):
        self.id = id
        self.name = name
        self.subjects = subjects
        self.topics = topics

    def addSubject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

    def addInterestedTopic(self, topic):                 ##key 1 in dict
        if 'interested_in_topics' not in self.topics:
            self.topics['interested_in_topics'] = []
        if topic not in self.topics['interested_in_topics']:
            self.topics['interested_in_topics'].append(topic)

    def addKnownTopic(self, topic):                      ##key 2 in dict
        if 'already_known_topics' not in self.topics:
            self.topics['already_known_topics'] = []
        if topic not in self.topics['already_known_topics']:
            self.topics['already_known_topics'].append(topic)   

    def printUser(self):
        print(f"id={self.id}, name={self.name}, subjects={self.subjects}, topics={self.topics}")  #f to evaluate inside the {}


    def changeName(self, new_name):
        self.name = new_name

    def deleteInterestedTopic(self, topic):
        if 'interested_in_topics' in self.topics and topic in self.topics['interested_in_topics']:
            self.topics['interested_in_topics'].remove(topic)

    def deleteKnownTopic(self, topic):
        if 'already_known_topics' in self.topics and topic in self.topics['already_known_topics']:
            self.topics['already_known_topics'].remove(topic)
            
    def deleteUser(users, user_id):
        for user in users:
         if user.id == user_id:
            users.remove(user)
            break