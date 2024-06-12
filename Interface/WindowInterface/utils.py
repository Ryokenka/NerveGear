import csv


def load_selected_options():
    print("je load")
    with open("../ConfigEngine/selected_options.txt", 'r') as file:
        reader = csv.reader(file)
        config = []
        for row in reader:
            selected = row[0]
            config.append(selected)
        return config

def load_capteurs_list():
    config = []
    try:
        with open("../ConfigEngine/capteurs_list.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Vérifiez que la ligne n'est pas vide
                    config.append(row[0])
    except FileNotFoundError:
        print("The file capteurs_list.csv does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return config


def write_selected_options(choice, i):
    print("write")
    with open('../ConfigEngine/selected_options.txt', 'r') as f:
        lines = f.readlines()
    with open('../ConfigEngine/selected_options.txt', 'w') as f:
        for j, line in enumerate(lines):
            if j == i:
                f.write(f'{choice}\n')
            else:
                f.write(line)