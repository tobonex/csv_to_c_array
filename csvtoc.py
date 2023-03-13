import argparse

def csvtoc(output,input):
    import csv
    with open(input, newline='') as csvfile:
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
        with open(output, "w") as file:
            file.write(buf)
            file.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='csvtoc',
        description='Parse csv data into c array',
        epilog='')
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()
    print(args.input_file)
    print(args.output_file)
    csvtoc(args.output_file, args.input_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
