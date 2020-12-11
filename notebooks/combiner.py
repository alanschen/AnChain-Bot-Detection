import numpy as np

def majority_vote(lst):
    """
    Input: list that contains member votes for 
    """
    lst = list(lst)
    counts = np.unique(lst, return_counts=True)
    if(len(counts[0]) == 1):
        return counts[0]
    if counts[1][0] == counts[1][1]:S
        return 'tied'
    else:
        return counts[0][np.argmax(counts[1])]
    
def convert_label(i):
    if i == 0:
        return 'bot'
    return 'human'
