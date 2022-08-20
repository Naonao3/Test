def frogPosition(leaves,jumps,start):
    # 関数を完成させてください
    postion = (jumps + start) % leaves
    if postion == 0:
        return leaves
    else:
        return postion