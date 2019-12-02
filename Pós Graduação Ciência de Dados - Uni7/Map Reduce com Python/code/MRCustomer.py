from mrjob.job import MRJob

class MRCustomer (MRJob):
    def mapper(self, _, line):
        customerID, _, amount = line.split(',')
        yield customerID, float(amount)

    def reducer(self, customerID, values):
        amounts = list(values)
        yield customerID, sum(amounts) / len(amounts)

if __name__ == '__main__':
    MRCustomer.run()