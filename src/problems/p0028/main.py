def f(dim):
    # Takes only positive, odd integers!
    if dim == 1:
        return 1
    else:
        c = (dim)**2
        return sum([c-(dim-1)*i for i in range(4)]) + f(dim-2)

def main():
    return f(1001)
