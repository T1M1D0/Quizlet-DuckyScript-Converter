import re

#Functions are sloppy they are just made to make it easier to read
#Not a great Programmer, very sloppy code

def rw():
    with open('convert.txt', 'r') as convert:
        word_list_raw = convert.read()
    word_list_raw = re.split('[:\n]', word_list_raw)
    word_list = [key.strip() for key in word_list_raw]
    ducky_conv(word_list)

def ducky_conv(wL):
    with open('quizlet.txt', 'w', encoding='utf-8') as f:
        f.write('DEFAULTDELAY 1000\n')
        for p in range(len(wL)):
            f.write('STRING ' + wL[p] + '\n')
            f.write('TAB\n')
            p+=1

def main():
    output = 'quizlet.txt'
    print("Upload a file called 'convert.txt' and populate it with what words you want to convert")
    print("If this is done, enjoy your new script to finish your quizlet which will be found in the 'quizlet.txt file'")
    rw()

if __name__ == "__main__":
    main()
