from os import strerror

mydict = {}
value = 1
fileName = input("please enter the file name(including the extension):")


def processChar(char):
    if char.isalpha():
        # as requested by the exercise, upper case and lower case are treated equally
        # forcing the char to be lowercase.
        lowerChar = char.lower()
        # try to find the key value (lowerChar) in mydict
        if lowerChar in mydict:
            mydict[lowerChar] += value
        else:
                # if the key is not in mydict yet, put into mydict and assign
                # value = 1
            mydict[lowerChar] = value
    else:
        print("excliding non-latin characters:", char, " is not a letter!")


try:
    stream = open(fileName, "rt")
    char = stream.read(1)
    while char != "":
        processChar(char)
        char = stream.read(1)
    stream.close()
    for char, frequency in mydict.items():
        print(char, "--->", frequency)
except IOError as e:
    print("The file can't be read:", strerror(e.errno))
