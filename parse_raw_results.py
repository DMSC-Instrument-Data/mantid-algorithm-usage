import json
import config


def load_raw_results():
    with open(config.cache_dir + '/raw-results', 'r') as myfile:
        return json.loads(myfile.read())


class AlgResultRecord:
    def __init__(self, entries):
        self.name = entries[0]
        self.count = entries[1]
        self.is_child = entries[2]
        self.version = entries[3]


def get_algorithm_results():
    lines = load_raw_results()
    records = []
    for line in lines:
        records.append(AlgResultRecord(line))
    return records


for record in get_algorithm_results():
    print('{} {} {} {}'.format(record.name, record.count, record.is_child, record.version))
