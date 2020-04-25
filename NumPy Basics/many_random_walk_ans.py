import random
import numpy as np

RANDOM_GENERATION_TYPES = ['rand', 'randint', 'normal']
DEV_RANDOM_TYPES = ['normal']
WALK_NUMBER = 5000
THRESHOLD = 30
NUMBER_OF_STEPS = 500
NOT_REACHED_MESSAGE = 'not reached'

def rand(number_of_walks, number_of_steps): 
    steps = np.array([[1 if random.randint(0, 1) else -1 for j in range(number_of_steps + 1)] for i in range(number_of_walks)])
    return steps

def randint(number_of_walks, number_of_steps): 
    steps = np.random.randint(0, 2, size=(number_of_walks, number_of_steps + 1), dtype='int')
    steps = np.where(steps > 0, 1, -1)
    return steps

def normal(number_of_walks, number_of_steps): 
    steps = np.random.normal(0, 2, size=(number_of_walks, number_of_steps + 1))
    steps = np.where(steps > 0, 1, -1)
    return steps

RANDOM_GENERATION_TYPES_SWITCHER = {
     'rand': rand,
     'randint': randint,
     'normal': normal,
}

def get_steps(generator_type, number_of_walks, number_of_steps):
    callback = RANDOM_GENERATION_TYPES_SWITCHER.get(generator_type, 'nothing')
    if (callback == 'nothing'): return rand(number_of_walks, number_of_steps)
    return callback(number_of_walks, number_of_steps)

def many_random_walk_ans(number_of_walks, number_of_steps, generator_algorithm = 'rand'):
    steps = get_steps(generator_algorithm, number_of_walks, number_of_steps);
    steps[:, 0] = 0
    walk_values = np.cumsum(steps, axis = 1)
    return walk_values

def find_minimum_transition(positions, transition_value):
    transition_times = np.full(shape = (positions.shape[0]), fill_value = np.nan)
    for i, walker in enumerate(positions):
        iterator = np.nditer(walker, flags=['c_index'])
        while not iterator.finished:
            positiove_iterator_value = abs(iterator[0])
            if positiove_iterator_value >= transition_value:
                transition_times[i] = iterator.index
                break
            iterator.iternext()
        pass
    transition_times_without_nan = transition_times[np.logical_not(np.isnan(transition_times))];
    if transition_times_without_nan.size == 0 : return NOT_REACHED_MESSAGE
    return transition_times_without_nan.min()

for generator_algorithm in RANDOM_GENERATION_TYPES:
    print('Algorithm:', generator_algorithm)
    positions = many_random_walk_ans(WALK_NUMBER, NUMBER_OF_STEPS, generator_algorithm)
    print('Min:', positions.min(), 'Max:', positions.max())
    print('Minimum transition time through', THRESHOLD, ':', find_minimum_transition(positions, THRESHOLD))