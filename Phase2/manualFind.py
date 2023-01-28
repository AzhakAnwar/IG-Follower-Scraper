with open('name', 'r+', errors = 'ignore') as fp:
    keys = fp.read().split('\n')
    new = ''
    for i in keys:
        if "'s profile picture" in i:
            new += i[:i.find("'s profile pictu")] + '",\n"'
    fp.seek(0)
    fp.truncate()

    fp.write(new)
    
