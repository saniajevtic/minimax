# Exercise from
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/

# A simple Python3 program to find
# maximum score that
# maximizing player can get

def minimax (curDepth, nodeIndex,
             maxTurn, scores,
             targetDepth):
    # curDepth is depth/level where game starts e.g. 0 is at root nodeIndex
    # nodeIndex is index of current node e.g. 0 is root nodeIndex
    # maxTurn = True means you are the maximising player (else minimizing)
    # scores is a list of scores of the final (target) player
    # targetDepth is the depth/level of the final (score) layer

    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,
                    False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                    False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,
                     True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                     True, scores, targetDepth))


# This code is contributed
# by rootshadow
