def add_ingot(purse):
	newDict = dict()
	newDict['gold_ingots'] = purse['gold_ingots']
	return newDict

def get_ingot(purse):
	newDict = dict()
	newDict['gold_ingots'] = purse['gold_ingots'] + 1
	return newDict


def empty(purse):
	return {'gold_ingots': 0}	
