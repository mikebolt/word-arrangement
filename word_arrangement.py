import math

def get_best_arrangement(L, wordlengths, space_size):
    best_results = [[None] * len(wordlengths) for _ in range(L)]
    line_lengths = get_best_arrangement_helper(L, wordlengths, space_size, 0, 0, best_results)[2]
    i = 0
    result = []
    for line_length in line_lengths:
        result.append(wordlengths[i : i + line_length])
        i += line_length
    return result

def get_best_arrangement_helper(L, wordlengths, space_size, l, i, best_results):
    if best_results[l][i] != None:
        return best_results[l][i]

    if l == L - 1:
        remaining_wordlengths = wordlengths[i:]
        num_remaining_words = len(remaining_wordlengths)
        length = sum(remaining_wordlengths) + (num_remaining_words - 1) * space_size
        best_results[l][i] = (length, length, [num_remaining_words,])
        return best_results[l][i]
    else:
        j = i
        current_length = 0
        num_words = len(wordlengths)
        
        best_ratio = math.inf
        best_min = 0
        best_max = 0
        best_arrangement = []
        
        while j < num_words - L + l + 1:
            current_length += wordlengths[j]
            if j > i:
                current_length += space_size
            j += 1
            
            subresult = get_best_arrangement_helper(L, wordlengths, space_size, l + 1, j, best_results)
            
            new_min = min(current_length, subresult[0])
            new_max = max(current_length, subresult[1])
            
            ratio = new_max / new_min
            
            if ratio < best_ratio:
                best_min = new_min
                best_max = new_max
                best_ratio = ratio
                best_arrangement = [j - i,] + subresult[2]

        best_results[l][i] = (best_min, best_max, best_arrangement)
        return best_results[l][i]
        
# print(get_best_arrangement(3, [3, 4, 3, 5, 5, 4, 1, 3, 2, 6, 4, 3, 4], 1))
