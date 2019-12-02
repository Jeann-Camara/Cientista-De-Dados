from mrjob.job import MRJob

class MRFakeFriends(MRJob):
    def mapper(self, _, line):
        _, _, age, numberOfFriends = line.split(',')
        yield age, int(numberOfFriends)

    def reducer(self, key, values):
        numberOfFriends = list(values)

        yield key, sum(numberOfFriends) / len(numberOfFriends)

if __name__ == "__main__":
    MRFakeFriends.run()



