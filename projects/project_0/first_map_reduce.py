from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordCount(MRJob):

    def mapper(self, key, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def reducer(self, word, count):
        yield word, sum(count)

if __name__ == '__main__':
    MRWordCount.run()