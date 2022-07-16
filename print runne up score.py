# print runner up score
if __name__ == '__name__':
    n = int(input("masukkan angka: "))
    # function map to allows you to process and transform all the items in an iterable without using an explisit for loop
    arr = map(int, input().split())
    print(sorted(list(set(arr))[-2]))
