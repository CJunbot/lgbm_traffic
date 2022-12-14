import pandas as pd
from haversine import haversine

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 400)

train = pd.read_parquet('../data/train_bus.parquet')
test = pd.read_parquet('../data/test.parquet')
bus_station = pd.read_csv('../../jeju_bus.csv', encoding='cp949')


test['start_bus_km'] = 0
test['end_bus_km'] = 0

for trains in range(0, 800000):
    start = (train['start_latitude'][trains], train['start_longitude'][trains])
    start2 = (train['end_latitude'][trains], train['end_longitude'][trains])
    min1, min2 = 1000, 1000
    print(trains)
    for bus in range(len(bus_station)):
        end = (bus_station['long'][bus], bus_station['lati'][bus])
        cash_start = haversine(start, end)
        cash_end = haversine(start2, end)
        if cash_start < min1:
            min1 = cash_start
        if cash_end < min2:
            min2 = cash_end
    train['start_bus_km'][trains] = min1
    train['end_bus_km'][trains] = min2

for trains in range(len(test)):
    start = (test['start_latitude'][trains], test['start_longitude'][trains])
    start2 = (test['end_latitude'][trains], test['end_longitude'][trains])
    min1, min2 = 1000, 1000
    print(trains)
    for bus in range(len(bus_station)):
        end = (bus_station['long'][bus], bus_station['lati'][bus])
        cash_start = haversine(start, end)
        cash_end = haversine(start2, end)
        if cash_start < min1:
            min1 = cash_start
        if cash_end < min2:
            min2 = cash_end
    test['start_bus_km'][trains] = min1
    test['end_bus_km'][trains] = min2

test.to_parquet('../../data/test_bus.parquet', index=False)
train.to_parquet('../../data/train_bus1.parquet', index=False)
