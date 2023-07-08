def load_data(file_path):
    data = []
    with open(f"{file_path}", "r") as file:
        data = file.read().splitlines()
    return data
    
first_names = load_data('src/first_names.txt')
last_names = load_data('src/last_names.txt')
cities = load_data("src/cities.txt")
gus = load_data("src/gus.txt")
cafe_types = load_data("src/cafe_types.txt")
cafe_districts = load_data("src/cafe_districts.txt")