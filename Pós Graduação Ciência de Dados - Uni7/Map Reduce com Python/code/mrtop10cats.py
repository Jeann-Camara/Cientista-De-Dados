from mrjob.job import MRJob
from mrjob.step import MRStep
class MRTop10Cats(MRJob):
    top10 = []

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                reducer_init=self.reducer_init),
            MRStep(reducer=self.reducer) 
        ]

    #<cat_weight><,><cat_id><;><cat_name>
    def mapper(self, _, line):
        weight, catID, carName = line.split(",")

        self.top10.append((float(weight), line))
        if len(self.top10) > 10:
            self.top10.sort()
            self.top10.pop(0)

    def reducer_init(self):
        for item in self.top10:
            yield None, item

    def reducer(self, key, values):
        print('REDUCER')
        finaltop10 = []

        items = list(values)

        for item in items:
            finaltop10.append(item)

            if len(finaltop10) > 10:
                finaltop10.sort()
                finaltop10.pop(0)

        for item in finaltop10:
            yield None, item[1]

if __name__ == "__main__":
    MRTop10Cats.run()