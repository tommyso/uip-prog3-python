import re

if __name__ == '__main__':

    patron = '[a-ce-gi-oq-z0-9][a-z0-9][{a-df-qs-z}\s][{a-ce-z}\s]'
    palabras = ['rap them', 'tapeth', 'apth', 'wrap/try', 'sap tray', '87ap9th', 'apothecary', 'aleht', 'happy them', 'tarpth', 'Apt', 'peth', 'tarreth', 'ddpdg']

    for palabra in palabras:
        if re.match(patron, palabra):
            print("La palabra " + palabra + " cumple.")
        else:
            print("La palabra " + palabra + " no cumple.")
