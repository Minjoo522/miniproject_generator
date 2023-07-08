import csv

def read_csv_uuid(file_path):
    uuid_list = []
    with open(f"{file_path}.csv", "r") as file:
        uuids = csv.reader(file)
        next(uuids) # 헤더 스킵
        for uuid in uuids:
            uuid_list.append(uuid[0])
    return uuid_list

user_uuids = read_csv_uuid("dataset/user")
store_uuids = read_csv_uuid("dataset/store")
item_uuids = read_csv_uuid("dataset/item")
order_uuids = read_csv_uuid("dataset/order")