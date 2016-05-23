"""Write a story, one line at a time"""

f = open('story.txt', 'a')

line = input('First line (hit enter to quit): ')

while line != '':
    f.write(line + '\n')
    line = input('Next line: ')

f.close()
