'''Purses for trolls'''
def squeak(func):
    '''Decorator which decorate troll functions'''
    def wraper(*args, **kwargs):
        print('SQUEAK')
        func(*args, **kwargs)
    return wraper

@squeak
def add_ingot(purse):
    '''Increase number of ingots by one'''
    new_dict = purse.copy()
    if 'gold_ingots' in new_dict.keys():
        new_dict['gold_ingots'] += 1
    else:
        new_dict['gold_ingots'] = 1
    return new_dict

@squeak
def get_ingot(purse):
    '''Decrease number of ingots by one'''
    new_dict = purse.copy()
    if 'gold_ingots' in new_dict.keys() and new_dict['gold_ingots'] != 0:
        new_dict['gold_ingots'] = new_dict['gold_ingots'] - 1
    return new_dict

@squeak
def empty(_purse):
    '''Clear purse'''
    return {}
    