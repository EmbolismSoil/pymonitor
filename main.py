from sample import OnlineAndCellStatis, AgvRecords


if __name__ == '__main__':
    sampler = OnlineAndCellStatis()
    sampler.sample()

    avg = AgvRecords()
    avg.sample()