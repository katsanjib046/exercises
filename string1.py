import time
def join1(document):
    """Combining letters from a document if they are alphabetical"""
    letters=''
    for c in document:
        if c.isalpha():
            letters += c
    return letters

def join2(document):
    """Combining letters from a document if they are alphabetical"""
    lst = []
    for c in document:
        if c.isalpha():
            lst.append(c)
    letters = ''.join(lst)
    return letters





if __name__ == "__main__":
    document = "So many different things are there. May be twenty (20) things. I want more things here so that it takes a lot \
        of time and we can basically check for everything we wanted. Lets try adding more and more words. Google LLC is an American\
             multinational technology company that focuses on search engine technology, online advertising,\
             cloud computing, computer software, quantum computing, e-commerce, artificial intelligence,\
                 and consumer electronics. Google LLC is an American multinational technology company that focuses\
                     on search engine technology, online advertising, cloud computing, computer software,\
                     quantum computing, e-commerce, artificial intelligence, and consumer electronics.\
                        Google LLC is an American multinational technologySo many different things are there. May be twenty (20) things. I want more things here so that it takes a lot \
        of time and we can basically check for everything we wanted. Lets try adding more and more words. Google LLC is an American\
             multinational technology company that focuses on search engine technology, online advertising,\
             cloud computing, computer software, quantum computing, e-commerce, artificial intelligence,\
                 and consumer electronics. Google LLC is an American multinational technology company that focuses\
                     on search engine technology, online advertising, cloud computing, computer software,\
                     quantum computing, e-commerce, artificial intelligence, and consumer electronics.\
                        Google LLC is an American multinational technologySo many different things are there. May be twenty (20) things. I want more things here so that it takes a lot \
        of time and we can basically check for everything we wanted. Lets try adding more and more words. Google LLC is an American\
             multinational technology company that focuses on search engine technology, online advertising,\
             cloud computing, computer software, quantum computing, e-commerce, artificial intelligence,\
                 and consumer electronics. Google LLC is an American multinational technology company that focuses\
                     on search engine technology, online advertising, cloud computing, computer software,\
                     quantum computing, e-commerce, artificial intelligence, and consumer electronics.\
                        Google LLC is an American multinational technologySo many different things are there. May be twenty (20) things. I want more things here so that it takes a lot \
        of time and we can basically check for everything we wanted. Lets try adding more and more words. Google LLC is an American\
             multinational technology company that focuses on search engine technology, online advertising,\
             cloud computing, computer software, quantum computing, e-commerce, artificial intelligence,\
                 and consumer electronics. Google LLC is an American multinational technology company that focuses\
                     on search engine technology, online advertising, cloud computing, computer software,\
                     quantum computing, e-commerce, artificial intelligence, and consumer electronics.\
                        Google LLC is an American multinational technologySo many different things are there. May be twenty (20) things. I want more things here so that it takes a lot \
        of time and we can basically check for everything we wanted. Lets try adding more and more words. Google LLC is an American\
             multinational technology company that focuses on search engine technology, online advertising,\
             cloud computing, computer software, quantum computing, e-commerce, artificial intelligence,\
                 and consumer electronics. Google LLC is an American multinational technology company that focuses\
                     on search engine technology, online advertising, cloud computing, computer software,\
                     quantum computing, e-commerce, artificial intelligence, and consumer electronics.\
                        Google LLC is an American multinational technology company that focuses on search engine technology, online advertising, cloud computing, computer software, quantum computing, e-commerce, artificial intelligence, and consumer electronics."

    n = 10
    total = 0
    for i in range(n):
        start = time.time()
        A = join1(document)
        end = time.time()
        total += (end - start)
    print(f"Method 1: {(total / n):.20f}")

    total = 0
    for i in range(n):
        start = time.time()
        A = join2(document)
        end = time.time()
        total += (end - start)
    print(f"Method 2: {(total / n):.20f}")
    