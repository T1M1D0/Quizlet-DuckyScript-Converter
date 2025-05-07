import re
import subprocess

#Functions are sloppy they are just made to make it easier to read
#Not a great Programmer, very sloppy code

def rw():
    with open('convert.txt', 'r') as convert:
        words = convert.read()
    subprocess.run(['/bin/bash', '/home/t1m1d/Code/Python/AutoQuiz/script.sh'])
    with open('converted.txt', 'r') as converted:
        words_list = converted.read()
    words_lists = re.split('[:;]', words_list)
    ducky_conv(words_lists)

def ducky_conv(wL):
    with open('quizlet.txt', 'w', encoding='utf-8') as f:
        f.write('DEFAULTDELAY 1000\n')
        for p in range(len(wL)):
            f.write('STRING ' + wL[p] + '\n')
            f.write('TAB\n')
            p+=1

def main():
    output = 'quizlet.txt'
    print("Upload a file called 'convert.txt' and populate it with what words you want to convert\n")
    rw()

if __name__ == "__main__":
    main()
