def changeunit(tmp):
    if tmp[0] == 'C':
        return 'Celsius','Fahrenheit',round(float(tmp[1:])*1.8 + 32,2)
    else:
        return 'Fahrenheit','Celsius',round((float(tmp[1:]) - 32) / 1.8,2)

def main():
    tmp = str(input('Please enter the temperature: '))
    tmp = tmp.upper()
    if tmp[0] not in ["C",'F'] or not tmp[1:].isnumeric():
        print("Invalid input. Please enter the temperature with the correct 'C' or F' prefix")
    else:
        changed = changeunit(tmp)
        print("%s degrees %s is converted to %s degrees %s"%(tmp, changed[0], changed[2], changed[1]))

if __name__ == '__main__':
    main()


