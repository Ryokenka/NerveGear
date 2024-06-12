config_path = "../ConfigEngine/selected_options.txt"

def config_to_code(config_path):
    code = ""
    try:
        with open(config_path, 'r') as file:
            for line_number, line in enumerate(file):
                
                # Déplacement (touches flechees)
                if line_number == 0:
                    if "Veuillez choisir" in line:
                        code += "0"
                    elif "Camera" in line:
                        code += "1"
                    elif "Accelerometre" in line:
                        code += "2"

                # Vitesse
                if line_number == 1:
                    if "Veuillez choisir" in line:
                        code += "0"
                    elif "ECG - rythme cardiaque" in line:
                        code += "1"

                # Sauter (touche espace)     
                if line_number == 2:
                    if "Veuillez choisir" in line:
                        code += "0"
                    elif "EMG - bras 1 impulsions" in line:
                        code += "1"
                    elif "EMG - bras 2 impulsions" in line:
                        code += "2"
                    elif "EEG - clignement des yeux" in line:
                        code += "3"

                # Clique souris
                if line_number == 3:
                    if "Veuillez choisir" in line:
                        code += "0"
                    elif "EMG - bras 1 impulsions" in line:
                        code += "1"
                    elif "EMG - bras 2 impulsions" in line:
                        code += "2"

                # Changer d'objet en main
                if line_number == 4:
                    if "Veuillez choisir" in line:
                        code += "0"
                    elif "Camera - doigts" in line:
                        code += "1"
                    elif "Camera - Eye tracking" in line:
                        code += "2"

    except FileNotFoundError:
        print("📁 File not found!")
    except Exception as e:
        print("⚠️ An error occurred:", e)

    return code


def code_to_config(code, configuration_path):
    config = ""


    for line_number in range(5):

        # Déplacement (touches flechees)
        if line_number == 0:
            if '0' in code[line_number]:
                config += "Veuillez choisir\n"
            elif '1' in code[line_number]:
                config += "Camera\n"
            elif '2' in code[line_number]:
                config += "Accelerometre\n"

        # Vitesse
        if line_number == 1:
            if '0' in code[line_number]:
                config += "Veuillez choisir\n"
            elif '1' in code[line_number]:
                config += "ECG - rythme cardiaque\n"

        # Sauter (touche espace)
        if line_number == 2:
            if '0' in code[line_number]:
                config += "Veuillez choisir\n"
            elif '1' in code[line_number]:
                config += "EMG - bras 1 impulsions\n"
            elif '2' in code[line_number]:
                config += "EMG - bras 2 impulsions\n"
            elif '3' in code[line_number]:
                config += "EEG - clignement des yeux\n"

        # Clique souris
        if line_number == 3:
            if '0' in code[line_number]:
                config += "Veuillez choisir\n"
            elif '1' in code[line_number]:
                config += "EMG - bras 1 impulsions\n"
            elif '2' in code[line_number]:
                config += "EMG - bras 2 impulsions\n"

        # Changer d'objet en main
        if line_number == 4:
            if '0' in code[line_number]:
                config += "Veuillez choisir"
            elif '1' in code[line_number]:
                config += "Camera - doigts"
            elif '2' in code[line_number]:
                config += "Camera - Eye tracking"

    try:
        with open(configuration_path, 'w') as file:
            file.write(config)
        print("✅ Configuration écrite dans selected_options.txt")
    except Exception as e:
        print("⚠️ Une erreur est survenue lors de l'écritue de la config:", e)

# Exemple pour config_to_code
print(f'Code de config: {config_to_code(config_path)}')  # "01201"

# Exemple pour code_to_config
code = "00000"
config = code_to_config(code, config_path)
print(f' Texte de la config : {config}')