#!/usr/bin/python3
def best_score(a_dictionary):

    if (a_dictionary):
        best = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
        return best[0][0]

    return None
