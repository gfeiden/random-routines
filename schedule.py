#
#

def scheduleRandom(filename):
    """ randomly generate schedule for astro division assembly """
    import fileinput as _fi
    import numpy.random as npr

    people = [x for x in _fi.input(filename)]
    _fi.close()

    fout = open('new_schedule.txt', 'w')
    npr.seed()
    for i in range(len(people)):
        person = people.pop(int(npr.random()*(len(people) - 1)))
        fout.write(person)
        if i % 2 != 0:
            fout.write('\n')
    fout.close()
    return 

if __name__ == '__main__':
    import sys
    scheduleRandom(sys.argv[1])
