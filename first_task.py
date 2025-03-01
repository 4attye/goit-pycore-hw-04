def total_salary(path):
    try:

        with open(path, "r", encoding='utf-8') as file:
            lines = file.readlines()

        total_salarys = 0
        count = 0

        for line in lines:
            name, salary = line.strip().split(',')
            total_salarys += int(salary)
            count += 1

        average_salary = total_salarys / count
        return total_salarys, int(average_salary)

    except FileNotFoundError:
        return "File not found"

    except ValueError:
        return "Data processing error"


try:

    total, average = total_salary("path/to/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

except Exception:

    print(total_salary("path/to/salary_file.txt"))