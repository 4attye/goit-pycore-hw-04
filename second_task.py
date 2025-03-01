def get_cats_info(path):
    try:

        with open(path, "r", encoding='utf-8') as file:
            lines = file.readlines()

        list_of_dictionaries = []

        for line in lines:

            cat_id, cat_name, cat_age = line.strip().split(",")

            dictionery = {
                "id": cat_id,
                "name": cat_name,
                "age": cat_age}

            list_of_dictionaries.append(dictionery)

        return list_of_dictionaries

    except FileNotFoundError:
        return "File not found"

    except ValueError:
        return "Data processing error"


try:

    cats_info = get_cats_info("path/to/cats_file.txt")
    print(cats_info)

except Exception:

    print(get_cats_info("path/to/cats_file.txt"))
