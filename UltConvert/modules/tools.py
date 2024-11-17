from modules.data import *




def any_base_to_dec(init_number, init_base):
    init_base = int(init_base)
    v1 = []
    for i in init_number:
        for b in char_map:
            if i == b:
                v1.append(
                    char_map.index(b)
                ) 

    target_number = 0
    a = len(v1) - 1

    for n in v1:
        n = int(n)
        target_number += n * init_base**a

        a -= 1  

    return target_number


def dec_to_any_base(init_number, target_base):
    target_number = ""
    n = int(init_number)
    target_base = int(target_base)

    while n > 0:
        a = n % target_base
        target_number += str(char_map[a])
        n //= target_base

    target_number = target_number[::-1]  
    return target_number



def check_inputs(init_number, init_base, target_base):
    error = None

    # Check if init_base and target_base are valid integers
    if not (isinstance(init_base, (str, int)) and isinstance(target_base, (str, int))):
        error = "Les bases doivent forcément être des nombres entiers"
        return error

    # Convert init_base and target_base to strings if they are integers
    if isinstance(init_base, int):
        init_base = str(init_base)
    if isinstance(target_base, int):
        target_base = str(target_base)

    # Check if the strings are numeric
    if not init_base.isnumeric() or not target_base.isnumeric():
        error = "Les bases doivent forcément être des nombres entiers"
        return error

    # Convert to integers
    init_base = int(init_base)
    target_base = int(target_base)

    # Check if the input base is valid
    if init_base < 2 or init_base > len(char_map):
        error = "La base d'entrée n'est pas valide. Le programme ne supporte que de la base 2 jusqu'à la base " + str(len(char_map))
        return error  # Return immediately if there's an error
    
    # Check if the target base is valid
    if target_base < 2 or target_base > len(char_map):
        error = "La base d'arrivée n'est pas valide. Le programme ne supporte que de la base 2 jusqu'à la base " + str(len(char_map))
        return error  # Return immediately if there's an error

    # Check if the init_number is valid for the specified init_base
    valid_chars = char_map[:init_base]  # Get valid characters for the input base
    for c in init_number:
        if c not in valid_chars:
            error = f"Le nombre d'entrée n'est pas valide. Le caractère {c} n'est pas autorisé dans la base {init_base}"
            break  # Exit the loop on the first error

    return error  # Return None if there are no errors

def converter(init_number, init_base, target_base):
    error = None
   
    error = check_inputs(init_number, init_base, target_base)

    if init_number == "0":
        return init_number, error
    if not error:
        init_number = any_base_to_dec(init_number, init_base)
        init_number = dec_to_any_base(init_number, target_base)
    return init_number, error







