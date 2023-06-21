'''Purses for trolls'''
def split_boty(*args):
    '''Split ingots equally between trolls'''
    my_sum = 0
    for purse in args:
        my_sum += (purse.get('gold_ingots', 0))
    result_dicts = []
    ingots = []
    ingots.append(int(my_sum / 3 ))
    ingots.append(int((my_sum - ingots[0])/ 2))
    ingots.append(my_sum - ingots[0] - ingots[1])
    for i in ingots:
        result_dicts.append({'gold_ingots':i})
    return result_dicts
