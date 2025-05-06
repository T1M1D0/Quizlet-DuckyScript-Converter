import re

def main():
    output = 'quizlet.txt'
    words_list = input("Type the words you want to split into a text file to convert to duckyscript:\n")
    word = re.split('[:-]', words_list)
    print(word)
    with open(output, 'w', encoding='utf-8') as f:
        f.write('DEFAULTDELAY 1000\n')
        for p in range(len(word)):
            f.write('STRING ' + word[p] + '\n')
            f.write('TAB\n')
            p+=1

if __name__ == "__main__":
    main()
