def square_digits(num):
    num = str(num)
    res = 0
    chain_pre = []
    chain_res = []
    for i in num:
        res = int(i)**2
        chain_pre.append(str(res))
    chain_res = [''.join(chain_pre)]
    res = int(chain_res[0])
    return(res)