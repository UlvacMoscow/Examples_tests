""" You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.
    Input: Placed pawns coordinates as a set of strings.
    Output: The number of safe pawns as a integer.
    Example:
    safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
"""


def safe_pawns(pawns: set) -> int:
    safe_coords = [(chr(ord(x[0])-1) + str(int(x[1])-1),\
            chr(ord(x[0])+1) + str(int(x[1])-1)) for x in pawns]
    count = 0
    for pos in safe_coords:
      if pos[0] in pawns or pos[1] in pawns:
        count += 1

    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
