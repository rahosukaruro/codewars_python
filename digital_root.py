def digital_root(n):
    # ...
    integer_list = [int(x) for x in str(n)]
    
    while len(integer_list) != 1:
        n = sum(integer_list)
        integer_list = [int(x) for x in str(n)]

    return n