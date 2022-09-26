from typing import List

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        
        n = len(pieces)
        rook_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        bishop_moves = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        
        moves = {
            'rook': rook_moves + [(0,0)],
            'bishop': bishop_moves + [(0, 0)],
            'queen': rook_moves + bishop_moves + [(0, 0)]
        }
        
        def count(positions, directions):
            if all(direction == (0, 0) for direction in directions):
                return 0
            
            new_pos = [(i+di, j+dj) for (i,j),(di, dj) in zip(positions, directions)
                      if 0<i+di<9 and 0<j+dj<9]
            
            if len(set(new_pos)) != n:
                return 0
            
            number = 1
            for new_direction in get_directions(directions, 0, []):
                number += count(new_pos, new_direction)
                
            return number
        
        def get_directions(dirs, curr, stack):
            if len(stack) == n:
                yield stack
                return
            for i in range(curr, n):
                stack.append(dirs[i])
                for d in get_directions(dirs, i+1, stack):
                    yield d
                stack.pop()
                if any(dirs[i]):
                    stack.append((0, 0))
                    for d in get_directions(dirs, i + 1, stack):
                        yield d
                    stack.pop()
                    
        def initial(stack):
            number = 0
            if len(stack) == n:
                number += count(positions, stack)
            else:
                new_pc = pieces[len(stack)]
                for direction in moves[new_pc]:
                    stack.append(direction)
                    number += initial(stack)
                    stack.pop()
                    
            return number
        
        return initial([]) + 1