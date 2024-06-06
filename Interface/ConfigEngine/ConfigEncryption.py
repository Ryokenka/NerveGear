config_path = "selected_options.txt"

def config_to_code(config_path):
    code = ""
    try:
        with open(config_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                
                # Déplacement (touches flechees)
                if line_number == 0:
                    if "Veuillez choisir" in line:
                        code += "0"
                    if "Camera" in line:
                        code += "1"
                    if "Accelerometre" in line:
                        code += "2"

                # Vitesse
                if line_number == 1:
                    if "Veuillez choisir" in line:
                        code += "0"
                    if "ECG - rythme cardiaque" in line:
                        code += "1"

                # Sauter (touche espace)     
                if line_number == 2:
                    if "Veuillez choisir" in line:
                        code += "0"
                    if "EMG - bras 1 impulsions" in line:
                        code += "1"
                    if "EMG - bras 2 impulsions" in line:
                        code += "2"
                    if "EEG - clignement des yeux" in line:
                        code += "3"

                # Clique souris
                if line_number == 3:
                    if "Veuillez choisir" in line:
                        code += "0"
                    if "EMG - bras 1 impulsions" in line:
                        code += "1"
                    if "EMG - bras 2 impulsions" in line:
                        code += "2"

                # Changer d'objet en main
                if line_number == 4:
                    if "Veuillez choisir" in line:
                        code += "0"
                    if "Camera - doigts" in line:
                        code += "1"
                    if "Camera - Eye tracking" in line:
                        code += "2"

    except FileNotFoundError:
        print("📁 File not found!")
    except Exception as e:
        print("⚠️ An error occurred:", e)

    return code


def code_to_config(code):
    config = ""

    for line_number in range(5):

        if line_number == 0:
            if '0' in code:
                config += "Veuillez choisir\n"
            if '1' in code:
                config += "Camera\n"
            if '2' in code:
                config += "Accelerometre\n"

        elif line_number == 1:
            if '0' in code:
                config += "Veuillez choisir\n"
            if '1' in code:
                config += "ECG - rythme cardiaque\n"

        elif line_number == 2:
            if '0' in code:
                config += "Veuillez choisir\n"
            if '1' in code:
                config += "EMG - bras 1 impulsions\n"
            if '2' in code:
                config += "EMG - bras 2 impulsions\n"
            if '3' in code:
                config += "EEG - clignement des yeux\n"

        elif line_number == 3:
            if '0' in code:
                config += "Veuillez choisir\n"
            if '1' in code:
                config += "EMG - bras 1 impulsions\n"
            if '2' in code:
                config += "EMG - bras 2 impulsions\n"

        elif line_number == 4:
            if '0' in code:
                config += "Veuillez choisir"
            if '1' in code:
                config += "Camera - doigts"
            if '2' in code:
                config += "Camera - Eye tracking"


    try:
        with open(config_path, 'w') as file:
            file.write(config)
        print("✅ Configuration écrite dans selected_options.txt")
    except Exception as e:
        print("⚠️ Une erreur est survenue lors de l'écritue de la config:", e)

# Exemple pour config_to_code
print(f'Code de config: {config_to_code(config_path)}')  # "01201"

# Exemple pour code_to_config
code = "01201" 
config = code_to_config(code)
print(f' Texte de la config : {config}') 