'''Purses for trolls'''
def add_ingot(purse):
    '''Increase number of ingots by one'''
    new_dict = purse.copy()
    if 'gold_ingots' in new_dict.keys():
        new_dict['gold_ingots'] += 1
    else:
        new_dict['gold_ingots'] = 1
    return new_dict

def get_ingot(purse):
    '''Decrease number of ingots by one'''
    new_dict = purse.copy()
    if 'gold_ingots' in new_dict.keys() and new_dict['gold_ingots'] != 0:
        new_dict['gold_ingots'] = new_dict['gold_ingots'] - 1
    return new_dict

def empty(_purse):
    '''Clear purse'''
    return {}

# print(add_ingot(get_ingot(add_ingot(empty({'gold_ingots': 0})))))
    