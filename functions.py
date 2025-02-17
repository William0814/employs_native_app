def get_employs(filepath='Employs.txt'):
    """ Read a text file and return the list of Employs items."""
    with open(filepath, 'r') as file:
        employs = file.readlines()
    return employs

def write_employs(employs_arg, filepath='Employs.txt'):
    """ Write the Employ items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(employs_arg)

def parse(feet_inches):
    """Calculate the feet and inches before print the result
        in meters"""
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    meters = (feet * 0.3048) + (inches * 0.0254)
    return f'{feet} feet and {inches} inches is: {meters} Meters.'