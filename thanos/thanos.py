import random

def snap(livingthings):
	unworthy = set(random.sample(range(len(livingthings)),int(len(livingthings)/2.)))
	return [livingthing for c, livingthing in enumerate(livingthings) if c in unworthy]