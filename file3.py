def TOH(n, src, dest, aux):
    if n == 1:
        print("Move disk 1 from source", src, "to destination", dest)
        return
    TOH(n-1, src, aux, dest)
    print("Move disk", n, "from source", src, "to destination", dest)
    TOH(n-1, aux, dest, src)


# Driver code
n = 4
TOH(n, 'A', 'B', 'C')
