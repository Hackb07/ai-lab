import math

# Minimax function with Alpha-Beta Pruning
def minimax(depth, node_index, is_maximizing_player, values, alpha, beta):
    # Terminal condition: leaf node
    if depth == 3:
        return values[node_index]

    if is_maximizing_player:
        best = -math.inf

        # Explore left and right children
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Prune
            if beta <= alpha:
                break
        return best

    else:
        best = math.inf

        # Explore left and right children
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Prune
            if beta <= alpha:
                break
        return best

# Example: leaf node values in a game tree
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Initial call
optimal_value = minimax(0, 0, True, values, -math.inf, math.inf)
print("The optimal value is:", optimal_value)
