def mountains_of_hoiyama(width):
    mysum = 0
    start = 1
    while width > 0:
        peak = divmod(width,2)[0]+1
        #print(f'my peak is {peak}')
        up = list(range(start,start+peak))
        down = list(range(up[-1]-1, start-1, -1))
        #print(f"my up is {up} and down is {down}")
        row = up + down
        mysum += sum(row)
        width -= 2
        start+= 2
        #print(row)
    return mysum
    #print(mysum)

print(mountains_of_hoiyama(44))