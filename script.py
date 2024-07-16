import argparse
import random
class FormatError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
def takenames():
    names=[]
    while(True):
        name=input("Introduce the name (jump of line to end) \n")
        if(name == ""):
            print(name)
            break
        else:
            for word in name:
                if len(name)<1:
                    raise FormatError(f"La línea no contiene palabras.")
            names.append(name)
    return names
def menu():
    T=True
    while (T):
        seltext="""
    OPTIONS
        1-Paste the names one by one
        2-Search for a names.txt file
        3-Format help
        4-Exit
    """
        sel = input(seltext)
        try:
            sel = int(sel)
        except ValueError:
            print("Must be a number between 1 and 4")
        finally:
            if(sel<1 or sel >5):
                raise FormatError("Must be a number between 1 and 4")
        if(sel==1):
            names=takenames()
            break
        if(sel==2):
            names=file('names.txt')
            break
        if(sel==3):
            FE="""
    You must write the list of names that will participate in the next format:
    The names must be separated by a jump of line.
    The names can contain any alfanumeric character (letter, number or underscore)
    Avoid leaving blank lines
Valid Example: 
    Diana4 Smith
    Fernanda6 Dupont
    Ian9 Martínez
    Julia10 Leblanc
    Carlos3 Johnson
    Hélène8 Rodríguez
    Gabriel7 Brown
"""
            print(FE)
        if(sel==4):
            exit()
    return names
def file(filename:str):
    try:
        file = open(filename, 'r')
        names=file.read()
        names=names.split('\n')
        return names
    except FileNotFoundError:
        print(f"Error: The file names.txt was not found.")
    except IsADirectoryError:
        print(f"Error: Expected a file but found a directory: names.txt.")
    except OSError as e:
        print(f"Error: The OS was unable to read names.txt ")
    except FormatError:
        FE="""
Error: The format is incorrect
    You must write the list of names that will participate in the next format:
    The names must be separated by a jump of line.
    The names can contain any alfanumeric character (letter, number or underscore)
    Avoid leaving blank lines
Valid Example: 
    Diana4 Smith
    Fernanda6 Dupont
    Ian9 Martínez
    Julia10 Leblanc
    Carlos3 Johnson
    Hélène8 Rodríguez
    Gabriel7 Brown
"""
        print(FE)
    finally:
        file.close()
def is_ordering_posible(n,g):
    ng=n%g+g # size of the greatest group
    if (n < 2*ng):
        return(False)
    elif (g<=1):
        return(False)
    else:
        return(True)
def randomize_people(l1,g:int):
    n=len(l1)
    l2 = ['0'] * n
    random.shuffle(l1)
    ng=n%g+g
    ngrupos=((n-ng)//g)+1
    for i in range(0,n):
        if (i<ng):
            l2[(n-ng)+i]=l1[i] #First group is arranged to the end
        else:
            l2[(i-ng)]=l1[i]    #Rest of the groups are moved to the beginning
    return l2
def procesar_grupo(indices, l1, l2):
    grupo1 = []
    grupo2 = []
    for i in indices:
        grupo1.append(l1[i])
        grupo2.append(l2[i])
        grupo1.append(" ")
        grupo2.append(" ")
    grupo1.append('\n')
    grupo2.append('\n')
    
    for i in indices:
        with open(f'{l1[i]}.txt', 'w') as file:
            file.write("El grupo: " + ' '.join(grupo1) + "Regalais al grupo: " + ' '.join(grupo2))
def save_names(l1,l2,g:int):
    n = len(l1)
    gmax = n%g+g
#Primer grupo lo hacemos a mano
    procesar_grupo(range(0, gmax), l1, l2)
#El resto de grupos tendrán el mismo tamaño g
    for i in range(gmax,n,g): 
        procesar_grupo(range(i,i + g,1), l1, l2)
    print("Saved succesfully")
parser = argparse.ArgumentParser(
    prog='SecretSanta',
    description="This script allows the user to create files for the Secret Santa game, including the names of the participants and their assigned gift recipients.")
#Parser options management
parser.add_argument('-m','--menu',action='store_true', help='Shows a help menu with differents options of input')
parser.add_argument('-f', '--file',  help='Import names from a speciffic file')
parser.add_argument('-g','--groups',type=int,required=True, help='Indicate how many groups you want to divide people in')
args = parser.parse_args()
if(args.file == None):
    if(args.menu == True):
        l1=menu()
    else:
        raise FormatError(f"The file fild is empty")
else:
    l1=file(args.file)
if( not is_ordering_posible(len(l1),args.groups) ): #Check if groups can be made
    raise FormatError("The length of the array and the size of the group are incompatible")
#Reorder names(see function for more details)
l2=randomize_people(l1,args.groups)
#Finally save names
save_names(l1,l2,args.groups)