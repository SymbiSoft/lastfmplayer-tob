def sum(seq):
        def add(x,y): return x+y
        return reduce(add, seq, 0)