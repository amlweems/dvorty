dvorak = """`1234567890[]',.pyfgcrl/=\\aoeuidhtns-;qjkxbmwvz~!@#$%^&*(){}"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ """
qwerty = """`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>? """

def dtoq(s):
    return ''.join([qwerty[dvorak.index(i)] for i in s])

if __name__ == "__main__":
    try:
        while True:
            s = raw_input()
            print dtoq(s)
    except Exception as e:
        pass
