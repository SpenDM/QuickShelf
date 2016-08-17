import shelve
import sys

DEFAULT_SHELF = 'shelf.db'


def shelve_variables(variables, filename=DEFAULT_SHELF):
    try:
        s = shelve.open(filename)

        for index, variable in enumerate(variables):
            s[index] = variable

        s.close()

    except IOError:
        sys.stderr.write("Error writing to shelf file " + filename)


def unshelve_variables(variables, filename=DEFAULT_SHELF):

    try:
        s = shelve.open(filename)

        for index in range(len(variables)):
            variables[index] = s[index]

        s.close()

    except IOError:
        sys.stderr.write("Error reading from shelf file " + filename)
