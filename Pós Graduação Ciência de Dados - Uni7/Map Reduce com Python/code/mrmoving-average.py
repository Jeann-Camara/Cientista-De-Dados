from mrjob.job import MRJob
from mrjob.job import MRStep

class MRMovingAverage(MRJob):    
    #<name-as-string><,><timestamp><,><value-as-double>
    def mapper(self, _, line):
        name, timestamp, value = line.split(",")

        yield name, (timestamp, float(value))

    def reducer(self, key, values):
        self.windowSize = 2

        data = list(values)
        data.sort()

        sum = 0.0
        outputValue = None

        for i in range(0, len(data)):           
            sum += data[i][1]

            if i < self.windowSize:
                movingAverage = sum / (i + 1)
            else:
                sum -= data[i - self.windowSize][1]                
                movingAverage = sum / self.windowSize
                
            timestamp = data[i][0]
            outputValue = str(timestamp) + ', ' + str(movingAverage)                

            yield key, outputValue

if __name__ == "__main__":
    MRMovingAverage.run()