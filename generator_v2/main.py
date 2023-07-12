import csv

# Generators
from generators import *
from models.user import User

# def save_csv(data):
#     with open(f"{date_type}.csv", "a", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(data)

if __name__ == "__main__":

    print(OrderItemGenerator().generate())

    data_type = input("데이터 유형을 입력하세요 (User, Store, Item): ").lower()
    records = int(input("생성할 개수를 입력하세요: "))
    output_format = input("아웃풋 형태를 입력하세요 (csv or console): ").lower()




    # data = data_gen.generate_data(data_type, num_records)
    # print_data(data, output_format)