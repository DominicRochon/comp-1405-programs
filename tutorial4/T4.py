import helper
import datetime

def count_vowels(word: str):
    vowels = 0
    for i in word:
        if helper.vowel_check(i):
            vowels += 1
    
    return vowels

def number_of_hits(target, word):
    count = 0
    findPos = 0
    while not findPos == -1:
        findPos = word.find(target)
        if not findPos == -1:
            count += 1
            word = word[findPos+len(target):]
    
    return count
        

def dateFormat(d: str):
    info = d.split('/')
    x = datetime.datetime(int(info[2]), int(info[1]), int(info[0]))
    print(f'{x:%A}, {x:%B} {x:%d}, {x:%Y}')
    print(f'{x:%Y}/{x:%m}/{x:%d}')
    print(f'{x:%d}-{x:%m}-{x:%y} ({x:%h})')

def dateSlice(d: str):
    day = d[0:2]
    month = d[3:5]
    year = d[6:]
    shortenedYear = year[2:]

    print(month + "/" + day + "/" + year)
    print(year + '/' + month + '/' + day)
    print(day + '-' + month + '-' + shortenedYear)

def dateSplit(d: str):
    info = d.split('/')
    day = info[0]
    month = info[1]
    year = info[2]

    print(month + "/" + day + "/" + year)
    print(year + '/' + month + '/' + day)
    print(day + '-' + month + '-' + year[2] + year[3])

def main():
    #print(count_vowels('Apples'))
    #dateSlice("14/05/2015")
    #dateSplit("14/05/2015")
    # dateFormat("14/05/2015")
    print(number_of_hits("ok", "okay then I okay dokay cook"))

if __name__ == "__main__":
    # execute only if run as a script
    main()

