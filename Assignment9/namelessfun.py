#fun=lambda x: fun(x)
#print fun(3)
#map(lambda n: (lambda f,*a: f(f, *a))(lambda rec, n: 1 if n == 0 else n*rec(rec, n-1), n), range(10))
foo = [2]
print map(lambda x: foo.append(x), foo)
