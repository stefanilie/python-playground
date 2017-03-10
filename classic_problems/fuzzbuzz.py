# Write a Python program to print numbers from 1 to 100 except for multiples of 3 for which you should print "fuzz" instead,
# for multiples of 5 you should print 'buzz' instead and for multiples of both 3 and 5, you should print 'fuzzbuzz' instead.
def fuzz(i):
    print "fuzz", i

def buzz(i):
    print "buzz", i

def fuzzbuzz(i):
    print "fuzzbuzz", i


# This is the most non efficient method of solving this,
# but it's the quickest to implement.
def trivialAlgorithm():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            fuzzbuzz(i)
        elif i % 3 == 0:
            fuzz(i)
        elif i%5 == 0:
            buzz(i)
        else:
            print i

# This is a more elaborate way of solving this,
# that, tbh, I got from the internet. But i add it here, because it seems cool.
def touplesAlgorithm():
    for i in range(1, 101):
        t = ((15, "fuzzbuzz"), (3, "fuzz"), (5, "buzz"), (i, i))
        for (k, v) in t:
            if i%k == 0:
                print v
                break


print "Trivial Algorithm"
trivialAlgorithm();
print "\n\nTouples Algorithm"
touplesAlgorithm();
