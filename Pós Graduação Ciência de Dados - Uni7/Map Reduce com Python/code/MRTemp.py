from mrjob.job import MRJob

class MRTemp(MRJob):
    def mapper(self, _, line):
        location, timestamp, metric, value, _, _, _, _ = line.split(',')

        if metric == 'TMAX' or metric == 'TMIN':
            yield location, (metric, int(value))

    def reducer(self, key, values):
        temps = list(values)
        temps.sort()

        tmax = []
        tmin = []

        for metric in temps:
            if metric[0] == 'TMAX':
                tmax.append(metric[1])
            else:
                tmin.append(metric[1])
        
        yield key, (min(tmin), max(tmax))

if __name__ == "__main__":
    MRTemp.run()
