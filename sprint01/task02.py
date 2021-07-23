def filterBible(scripture, book, chapter):
    scrip = []
    for el in scripture:
        if el[:2] == book and el[2:5] == chapter:
            scrip.append(el)
    return scrip
