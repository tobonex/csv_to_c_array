
filename = 'dat.csv'

def csvtoc():
    import csv
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        buf = 'int array[][] ={ \r\n{'
        for idx,row in enumerate(spamreader):
            if idx != 0:
                buf += '\r\n,{'
            for idx2,entry in enumerate(row[0].split('\t')):
                if idx2!=0:
                    buf += ','
                buf+=entry

            buf += '}'
        buf += '\r\n};'
        print(buf)
        with open('dat.c', "w") as file:
            file.write(buf)
            file.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csvtoc()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
