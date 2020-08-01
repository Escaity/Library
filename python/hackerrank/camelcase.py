def camelcase(s):
    return sum(1 for c in s if c.isupper()) + 1
