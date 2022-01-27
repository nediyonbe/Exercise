import functools
def print_rangoli(size):
    # your code goes here
    width = 2 * 2 * (size-1) + 1
    
    for i in range(size): #97, 123
        #print(functools.reduce(lambda x, y:  str(chr(x)) + str(chr(y)), range(97, 97 + size + 1)))
        liste = list(range(97 + i, 97 + size + 1))
        liste_text = [chr(x) for x in liste]
        print(i)
        print(functools.reduce(lambda x, y:  x + '-' + y, liste_text))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)