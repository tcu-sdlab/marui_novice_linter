#!/usr/local/bin/python3.5 -tt

import random
import re
import sys

if __name__ == '__main__':
    RE_PARENTHESIS = re.compile(r'(\([^)]*\))')

    RE_UNDERSCORE = re.compile(r'_+')

    n, s = (input(),
            input(),
    )

    c0, c1 = 0, 0

    for i in RE_PARENTHESIS.split(s):
        if i.startswith('('):
            c1 += len([_ for _ in RE_UNDERSCORE.split(i[1:-1]) if len(_)])
        else:
            c0 = max(max(len(_) for _ in RE_UNDERSCORE.split(i)), c0)

    print(c0, c1)