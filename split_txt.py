import csv


def split_txt():
    # txt 파일을 읽고 txt 파일과 csv 파일로 추출할 예정.
    openFileTxt = open('har.txt', 'r', encoding='UTF-8')
    writeFileTxt = open('split_har.txt', 'w', encoding='UTF-8')
    # txt 파일 읽기 쓰기

    writeFileCsv = open('har_csv.csv', 'w', encoding='utf-8-sig', newline='')
    wr = csv.writer(writeFileCsv)

    lines = openFileTxt.readlines()
    person = ''

    for line in lines:
        line.lstrip()
        if line == '\n':
            continue
        if line.split()[0] == '---------------' and line.find('요일') != -1:
            continue
        if line[0] != '[':
            print(line)
            writeFileTxt.write(line)
            wr.writerow([line])
            continue

        line = line.replace("[", "")  # 이수연] 오후 10:21] 챠
        line = line.replace("]", "")  # 이수연 오후 10:21 챠
        line = line.rstrip('\n')
        split_line = line.split(maxsplit=3)
        print(split_line)

        if person == line.split()[0]:
            line = ' ' + split_line[3]
            # line = line.rstrip('\n')
        else:
            line = '\n' + split_line[0] + ',' + split_line[3]  # 이수연,챠
            person = split_line[0]
        writeFileTxt.write(line)
        wr.writerow([split_line[0], split_line[3]])
        print(line)

    openFileTxt.close()
    writeFileTxt.close()
    writeFileCsv.close()
