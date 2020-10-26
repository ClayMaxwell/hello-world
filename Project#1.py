def Mean(list):
    if not list:
        return 0
    amount = 0
    for num in list:
        amount += num
    return amount / len(list)
def Median(list):
    if not list:
        return 0
    samples = sorted(list.copy())
    if len(samples) % 2 == 1:
        return samples[int(len(samples) / 2)]
    else:
        return (samples[int(len(samples) / 2)] + samples[int(len(samples) / 2) - 1]) / 2
def Mode(list):
    if not list:
        return 0
    result = list[0]
    count = 0
    for num in list:
        if list.count(num) >= count:
            count = list.count(num)
            result = num
    return result
def main():
   List = [8, 9, 9, 2, 6, 14, 1, 3, 6, 9]
   print('List:', List)
   print('Mode:', Mode(List))
   print('Median:', Median(List))
   print('Mean:', Mean(List))
main()
