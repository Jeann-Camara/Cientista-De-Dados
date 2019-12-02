from mrjob.job import MRJob

class MRTempMinMax(MRJob):
    def mapper(self, _, line):
        location, timestamp, metric, value, _, _, _, _ = line.split(',')

        if metric == 'TMAX' or metric == 'TMIN':
            yield (location, metric), int(value)

    def reducer(self, key, values):
        metric = key[1]
        
        if metric == 'TMAX':
            yield key, max(values)
        else:
            yield key, min(values) 

if __name__ == "__main__":
    MRTempMinMax.run()