from Model import  Slots, Integer, sample_desc, Date, Float
from datetime import date

class OnlineAndCellStatis:
    def __init__(self):
        pass


    @sample_desc(name='online_and_cell_statis', y=[Integer, Integer])
    def sample(self):
        return [1, 2]


class AgvRecords:
    @sample_desc(name='avg_records', x=Date, y=[Float])
    def sample(self):
        return date.today().strftime('%Y-%m-%d'), [1.0]
