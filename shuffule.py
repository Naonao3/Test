def shuffledPositions(arr,shuffledArr):
    # 関数を完成させてください
    hashmap ={}
    result = []

    for i in range(len(shuffledArr)):
        hashmap[shuffledArr[i]] = i
    
    for i in range(len(arr)):
        result.append(hashmap[arr[i]])

    return result

print(shuffledPositions([2,32,45],[45,32,2]))