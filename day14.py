#! /usr/bin/env python

import time
 
def expand_recipe(recipes, locations, score_seq = None):
    cur_1 = recipes[locations[0]]
    cur_2 = recipes[locations[1]]
 
    new_scores = cur_1 + cur_2
    if new_scores > 9:
        new_scores = [new_scores / 10, new_scores % 10]
    else:
        new_scores = [new_scores]
 
    recipes += new_scores
    new_pos_1 = (cur_1 + 1 + locations[0]) % len(recipes)
    new_pos_2 = (cur_2 + 1 + locations[1]) % len(recipes)
 
    locations[0] = new_pos_1
    locations[1] = new_pos_2
 
    if score_seq is not None:
        # print str(recipes[-len(score_seq):])
        # print score_seq
        if recipes[-len(score_seq):] == score_seq:
            return len(recipes) - len(score_seq)
        elif recipes[-(len(score_seq) + 1):-1] == score_seq:
            return len(recipes) - len(score_seq) - 1
        else:
            return 0


my_input = 652601
recipes = [3, 7]
locations = [0, 1]
 
start = time.time()
while len(recipes) < my_input + 10:
    expand_recipe(recipes, locations)

print 'Time elapsed part 1: ' + str(time.time() - start)
print 'Answer to part 1: ' + ''.join([str(x) for x in recipes[my_input:]])

recipes = [3, 7]
locations = [0, 1]
len_before_input_found = 0
# my_input = 92510
# my_input = 652
start = time.time()
my_input_list = [int(x) for x in list(str(my_input))]
while not len_before_input_found:
    len_before_input_found = expand_recipe(recipes, locations, my_input_list)
print 'Time elapsed part 2: ' + str(time.time() - start)
 
print "Answer to part 2: " + str(len_before_input_found)