#!/usr/bin/env python
# -*- coding: utf-8 -*-
class board:
    class pawn:
        def __init__(self, location, texture, move_type, checks, check_temp):
            self.location = location
            self.texture = texture
            self.move_type = move_type
            self.checks = checks
            self.checks_temp = check_temp

    tower1 = pawn('A1', 'T', 'tower', '', '')
    horse1 = pawn('B1', 'H', 'horse', '', '')
    runner1 = pawn('C1', 'R', 'runner', '', '')
    hetman = pawn('D1', 'Q', 'hetman', '', '')
    king = pawn('E1', 'K', 'king', '', '')
    pawn1 = pawn('A2', 'P', 'pawn', '', '')
    empty = pawn('none', '_', 'none', '', '')
    tower11 = pawn('A8', 't', 'tower', '', '')
    horse11 = pawn('B8', 'h', 'horse', '', '')
    runner11 = pawn('C8', 'r', 'runner', '', '')
    hetman1 = pawn('D8', 'q', 'hetman', '', '')
    king1 = pawn('E8', 'k', 'king', '', '')
    pawn11 = pawn('A7', 'p', 'pawn', '', '')

    class dataclass:
        def __init__(self, numbers_vector, numbers_row, insert_place, numbers_row_int, number_row_reversed,
                     insert_place_reversed):
            self.numbers_vector = numbers_vector
            self.numbers_row = numbers_row
            self.insert_place = insert_place
            self.numbers_row_ints = numbers_row_int
            self.number_row_reversed = number_row_reversed
            self.insert_place_reversed = insert_place_reversed

    data = dataclass(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], ['1', '2', '3', '4', '5', '6', '7', '8'],
                     {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, }, [1, 2, 3, 4, 5, 6, 7, 8],
                     [8, 7, 6, 5, 4, 3, 2, 1], {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'})

    def insert(self, pawn, place, board):
        pawn.location = place
        for i in self.data.numbers_row:
            if i in pawn.location:
                for x in self.data.numbers_vector:
                    if x in pawn.location:
                        board[self.data.number_row_reversed[int(i) - 1] - 1].pop(self.data.insert_place.get(x))
                        board[self.data.number_row_reversed[int(i) - 1] - 1].insert(self.data.insert_place.get(x),
                                                                                    pawn.texture)
                        return board

    def is_pawn_here(self, loc, board):
        try:
            for i in self.data.numbers_row:
                if i in loc:
                    for x in self.data.numbers_vector:
                        if x in loc:
                            if board[self.data.number_row_reversed[int(i) - 1] - 1][
                                self.data.insert_place.get(x)] != '_':
                                return board[self.data.number_row_reversed[int(i) - 1] - 1][
                                    self.data.insert_place.get(x)]
                            else:
                                return False
        except TypeError:
            return False

    def move(self, pawn, _from, to, board, type):
        pos = []
        horse_dict1 = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H'}
        horse_dict2 = {'H': 'G', 'G': 'F', 'F': 'E', 'E': 'D', 'D': 'C', 'C': 'B', 'B': 'A'}
        horse_dict3 = {'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H'}
        horse_dict4 = {'C': 'A', 'D': 'B', 'E': 'C', 'F': 'D', 'G': 'E', 'H': 'F'}
        for i in self.data.numbers_row:
            if i in _from:
                for x in self.data.numbers_vector:
                    if x in _from:
                        if pawn.move_type == 'pawn':
                            if ord(pawn.texture) < 100:
                                if i == '7':
                                    pos.append(x + str(int(i) - 2))
                                if self.is_pawn_here(x + str(int(i) - 1), board) == False:
                                    pos.append(x + str(int(i) - 1))
                                try:
                                    if self.is_pawn_here(horse_dict1.get(x) + str(int(i) - 1), board) != False and ord(
                                            self.is_pawn_here(horse_dict1.get(x) + str(int(i) - 1), board)) > 100:
                                        pos.append(horse_dict1.get(x) + str(int(i) - 1))
                                except TypeError:
                                    pass
                                try:
                                    if self.is_pawn_here(horse_dict2.get(x) + str(int(i) - 1), board) != False and ord(
                                            self.is_pawn_here(horse_dict2.get(x) + str(int(i) - 1), board)) > 100:
                                        pos.append(horse_dict2.get(x) + str(int(i) - 1))
                                except TypeError:
                                    pass
                            else:
                                if i == '2':
                                    pos.append(x + str(int(i) + 2))
                                if self.is_pawn_here(x + str(int(i) + 1), board) == False:
                                    pos.append(x + str(int(i) + 1))
                                try:
                                    if self.is_pawn_here(horse_dict1.get(x) + str(int(i) + 1), board) != False and ord(
                                            self.is_pawn_here(horse_dict1.get(x) + str(int(i) + 1), board)) < 100:
                                        pos.append(horse_dict1.get(x) + str(int(i) + 1))
                                except TypeError:
                                    pass
                                try:
                                    if self.is_pawn_here(horse_dict2.get(x) + str(int(i) + 1), board) != False and ord(
                                            self.is_pawn_here(horse_dict2.get(x) + str(int(i) + 1), board)) < 100:
                                        pos.append(horse_dict2.get(x) + str(int(i) + 1))
                                except TypeError:
                                    pass
                        if pawn.move_type == 'tower':
                            lock_up = False
                            lock_row = False
                            for a in range(1, 7):
                                if not lock_up:
                                    pos.append(x + str(int(i) + a))
                                if self.is_pawn_here(x + str(int(i) + a), board) != False:
                                    lock_up = True
                                    if (ord(self.is_pawn_here(x + str(int(i) + a), board)) > 100 and ord(
                                            pawn.texture) > 100) or (
                                            ord(self.is_pawn_here(x + str(int(i) + a), board)) < 100 and ord(
                                        pawn.texture) < 100):
                                        try:
                                            pos.pop()
                                        except IndexError:
                                            pass
                            for m in self.data.numbers_vector:
                                if not lock_row:
                                    pos.append(m + i)
                            if self.is_pawn_here(m + i, board) != False:
                                lock_row = True
                                if (ord(self.is_pawn_here(m + i, board)) > 100 and ord(pawn.texture) > 100) or (
                                        ord(self.is_pawn_here(m + i, board)) < 100 and ord(pawn.texture) < 100):
                                    pos.pop()
                        if pawn.move_type == 'horse':
                            try:
                                if self.is_pawn_here(horse_dict1.get(x) + str(int(i) + 2), board) != False:
                                    if (ord(self.is_pawn_here(horse_dict1.get(x) + str(int(i) + 2),
                                                              board)) > 100 and pawn.texture < 100) or (ord(
                                        self.is_pawn_here(horse_dict1.get(x) + str(int(i) + 2),
                                                          board)) < 100 and pawn.texture > 100):
                                        pos.append(horse_dict1.get(x) + str(int(i) + 2))
                            except TypeError:
                                pass
                            try:
                                if self.is_pawn_here(horse_dict2.get(x) + str(int(i) + 2), board) != False:
                                    if (ord(self.is_pawn_here(horse_dict2.get(x) + str(int(i) + 2),
                                                              board)) > 100 and pawn.texture < 100) or (ord(
                                        self.is_pawn_here(horse_dict2.get(x) + str(int(i) + 2),
                                                          board)) < 100 and pawn.texture > 100):
                                        pos.append(horse_dict2.get(x) + str(int(i) + 2))
                            except TypeError:
                                pass
                            try:
                                if self.is_pawn_here(horse_dict3.get(x) + str(int(i) + 1), board) != False:
                                    if (ord(self.is_pawn_here(horse_dict3.get(x) + str(int(i) + 1),
                                                              board)) > 100 and pawn.texture < 100) or (ord(
                                        self.is_pawn_here(horse_dict3.get(x) + str(int(i) + 1),
                                                          board)) < 100 and pawn.texture > 100):
                                        pos.append(horse_dict3.get(x) + str(int(i) + 1))
                            except TypeError:
                                pass
                            try:
                                if self.is_pawn_here(horse_dict4.get(x) + str(int(i) + 1), board) != False:
                                    if (ord(self.is_pawn_here(horse_dict4.get(x) + str(int(i) + 1),
                                                              board)) > 100 and pawn.texture < 100) or (ord(
                                        self.is_pawn_here(horse_dict4.get(x) + str(int(i) + 1),
                                                          board)) < 100 and pawn.texture > 100):
                                        pos.append(horse_dict4.get(x) + str(int(i) + 1))
                            except TypeError:
                                pass
                            try:
                                if self.is_pawn_here(horse_dict1.get(x) + str(int(i) - 2), board) != False:
                                    if (ord(self.is_pawn_here(horse_dict1.get(x) + str(int(i) - 2),
                                                              board)) > 100 and pawn.texture < 100) or (ord(
                                        self.is_pawn_here(horse_dict1.get(x) + str(int(i) - 2),
                                                          board)) < 100 and pawn.texture > 100):
                                        pos.append(horse_dict1.get(x) + str(int(i) - 2))
                            except TypeError:
                                pass
                            try:
                                if self.is_pawn_here(horse_dict2.get(x) + str(int(i) - 2), board) != False:
                                    if (ord(self.is_pawn_here(horse_dict2.get(x) + str(int(i) - 2),
                                                              board)) > 100 and pawn.texture < 100) or (ord(
                                        self.is_pawn_here(horse_dict2.get(x) + str(int(i) - 2),
                                                          board)) < 100 and pawn.texture > 100):
                                        pos.append(horse_dict1.get(x) + str(int(i) + 2))
                                pos.append(horse_dict2.get(x) + str(int(i) - 2))
                            except TypeError:
                                pass
                            try:
                                if self.is_pawn_here(horse_dict3.get(x) + str(int(i) - 1), board) != False:
                                    if (ord(self.is_pawn_here(horse_dict3.get(x) + str(int(i) - 1),
                                                              board)) > 100 and pawn.texture < 100) or (ord(
                                        self.is_pawn_here(horse_dict3.get(x) + str(int(i) - 1),
                                                          board)) < 100 and pawn.texture > 100):
                                        pos.append(horse_dict3.get(x) + str(int(i) - 1))
                            except TypeError:
                                pass
                            try:
                                if self.is_pawn_here(horse_dict4.get(x) + str(int(i) - 1), board) != False:
                                    if (ord(self.is_pawn_here(horse_dict4.get(x) + str(int(i) - 1),
                                                              board)) > 100 and pawn.texture < 100) or (ord(
                                        self.is_pawn_here(horse_dict4.get(x) + str(int(i) - 1),
                                                          board)) < 100 and pawn.texture > 100):
                                        pos.append(horse_dict1.get(x) + str(int(i) + 2))
                            except TypeError:
                                pass
                        if pawn.move_type == 'runner':
                            u = x
                            lock = False
                            for z in range(1, 8):
                                try:
                                    if not lock:
                                        pos.append(horse_dict1.get(u) + str(int(i) + z))
                                    if self.is_pawn_here(horse_dict1.get(u) + str(int(i) + z), board) != False:
                                        lock = True
                                        if (ord(self.is_pawn_here(horse_dict1.get(u) + str(int(i) + z),
                                                                  board)) > 100 and pawn.texture > 100) or (ord(
                                            self.is_pawn_here(horse_dict1.get(u) + str(int(i) + z),
                                                              board)) < 100 and pawn.texture < 100):
                                            pos.pop()
                                    u = horse_dict1.get(x)
                                except TypeError:
                                    pass
                            lock = False
                            u = x
                            for z in range(1, 8):
                                try:
                                    if not lock:
                                        pos.append(horse_dict1.get(u) + str(int(i) - z))
                                    if self.is_pawn_here(horse_dict1.get(u) + str(int(i) - z), board) != False:
                                        lock = True
                                        if (ord(self.is_pawn_here(horse_dict1.get(u) + str(int(i) - z),
                                                                  board)) > 100 and pawn.texture > 100) or (ord(
                                            self.is_pawn_here(horse_dict1.get(u) + str(int(i) - z),
                                                              board)) < 100 and pawn.texture < 100):
                                            pos.pop()
                                    u = horse_dict1.get(x)
                                except TypeError:
                                    pass
                            lock = False
                            u = x
                            for z in range(1, 8):
                                try:
                                    if not lock:
                                        pos.append(horse_dict2.get(u) + str(int(i) + z))
                                    if self.is_pawn_here(horse_dict2.get(u) + str(int(i) + z), board) != False:
                                        lock = True
                                        if (ord(self.is_pawn_here(horse_dict2.get(u) + str(int(i) + z),
                                                                  board)) > 100 and pawn.texture > 100) or (ord(
                                            self.is_pawn_here(horse_dict2.get(u) + str(int(i) + z),
                                                              board)) < 100 and pawn.texture < 100):
                                            pos.pop()
                                    u = horse_dict2.get(x)
                                except TypeError:
                                    pass
                            lock = False
                            u = x
                            for z in range(1, 8):
                                try:
                                    if not lock:
                                        pos.append(horse_dict2.get(u) + str(int(i) - z))
                                    if self.is_pawn_here(horse_dict2.get(u) + str(int(i) - z), board) != False:
                                        lock = True
                                        if (ord(self.is_pawn_here(horse_dict2.get(u) + str(int(i) - z),
                                                                  board)) > 100 and pawn.texture > 100) or (ord(
                                            self.is_pawn_here(horse_dict2.get(u) + str(int(i) - z),
                                                              board)) < 100 and pawn.texture < 100):
                                            pos.pop()
                                    u = horse_dict2.get(x)
                                except TypeError:
                                    pass
                        if pawn.move_type == 'hetman':
                            lock_up = False
                            lock_row = False
                            for a in range(1, 7):
                                if not lock_up:
                                    pos.append(x + str(int(i) + a))
                                if self.is_pawn_here(x + str(int(i) + a), board) != False:
                                    lock_up = True
                                    a1 = self.is_pawn_here(x + str(int(i) + a), board)
                                    if (ord(self.is_pawn_here(x + str(int(i) + a), board)) > 100 and ord(
                                            pawn.texture) > 100) or (
                                            ord(self.is_pawn_here(x + str(int(i) + a), board)) < 100 and ord(
                                        pawn.texture) < 100):
                                        pos.pop()
                            for m in self.data.numbers_vector:
                                if not lock_row:
                                    pos.append(m + i)
                                if self.is_pawn_here(m + i, board) != False:
                                    lock_row = True
                                    if (ord(self.is_pawn_here(m + i, board)) > 100 and ord(pawn.texture) > 100) or (
                                            ord(self.is_pawn_here(m + i, board)) < 100 and ord(pawn.texture) < 100):
                                        try:
                                            pos.pop()
                                        except IndexError:
                                            pass
                            u = x
                            lock = False
                            for z in range(1, 8):
                                try:
                                    if not lock:
                                        pos.append(horse_dict1.get(u) + str(int(i) + z))
                                    if self.is_pawn_here(horse_dict1.get(u) + str(int(i) + z), board) != False:
                                        lock = True
                                        if (ord(self.is_pawn_here(horse_dict1.get(u) + str(int(i) + z),
                                                                  board)) > 100 and pawn.texture > 100) or (ord(
                                            self.is_pawn_here(horse_dict1.get(u) + str(int(i) + z),
                                                              board)) < 100 and pawn.texture < 100):
                                            pos.pop()
                                    u = horse_dict1.get(x)
                                except TypeError:
                                    pass
                            lock = False
                            u = x
                            for z in range(1, 8):
                                try:
                                    if not lock:
                                        pos.append(horse_dict1.get(u) + str(int(i) - z))
                                    if self.is_pawn_here(horse_dict1.get(u) + str(int(i) - z), board) != False:
                                        lock = True
                                        if (ord(self.is_pawn_here(horse_dict1.get(u) + str(int(i) - z),
                                                                  board)) > 100 and pawn.texture > 100) or (ord(
                                            self.is_pawn_here(horse_dict1.get(u) + str(int(i) - z),
                                                              board)) < 100 and pawn.texture < 100):
                                            pos.pop()
                                    u = horse_dict1.get(x)
                                except TypeError:
                                    pass
                            lock = False
                            u = x
                            for z in range(1, 8):
                                try:
                                    if not lock:
                                        pos.append(horse_dict2.get(u) + str(int(i) + z))
                                    if self.is_pawn_here(horse_dict2.get(u) + str(int(i) + z), board) != False:
                                        lock = True
                                        if (ord(self.is_pawn_here(horse_dict2.get(u) + str(int(i) + z),
                                                                  board)) > 100 and pawn.texture > 100) or (ord(
                                            self.is_pawn_here(horse_dict2.get(u) + str(int(i) + z),
                                                              board)) < 100 and pawn.texture < 100):
                                            pos.pop()
                                    u = horse_dict2.get(x)
                                except TypeError:
                                    pass
                            lock = False
                            u = x
                            for z in range(1, 8):
                                try:
                                    if not lock:
                                        pos.append(horse_dict2.get(u) + str(int(i) - z))
                                    if self.is_pawn_here(horse_dict2.get(u) + str(int(i) - z), board) != False:
                                        lock = True
                                        if (ord(self.is_pawn_here(horse_dict2.get(u) + str(int(i) - z),
                                                                  board)) > 100 and pawn.texture > 100) or (ord(
                                            self.is_pawn_here(horse_dict2.get(u) + str(int(i) - z),
                                                              board)) < 100 and pawn.texture < 100):
                                            pos.pop()
                                    u = horse_dict2.get(x)
                                except TypeError:
                                    pass
                        if pawn.move_type == 'king':
                            if self.is_pawn_here(x + str(int(i) + 1), board) != False:
                                if (ord(self.is_pawn_here(x + str(int(i) + 1),
                                                          board)) > 100 and pawn.texture < 100) or (ord(
                                    self.is_pawn_here(x + str(int(i) + 1),
                                                      board)) < 100 and pawn.texture > 100):
                                    pos.append(x + str(int(i) + 1))
                            if self.is_pawn_here(x + str(int(i) - 1), board) != False:
                                if (ord(self.is_pawn_here(x + str(int(i) - 1),
                                                          board)) > 100 and pawn.texture < 100) or (ord(
                                    self.is_pawn_here(x + str(int(i) - 1),
                                                      board)) < 100 and pawn.texture > 100):
                                    pos.append(x + str(int(i) - 1))
                            if self.is_pawn_here(horse_dict2.get(x) + i, board) != False:
                                if (ord(self.is_pawn_here(horse_dict2.get(x) + i,
                                                          board)) > 100 and pawn.texture < 100) or (ord(
                                    self.is_pawn_here(horse_dict2.get(x) + i,
                                                      board)) < 100 and pawn.texture > 100):
                                    pos.append(horse_dict2.get(x) + i)
                            if self.is_pawn_here(horse_dict2.get(x) + i, board) != False:
                                if (ord(self.is_pawn_here(horse_dict1.get(x) + i,
                                                          board)) > 100 and pawn.texture < 100) or (ord(
                                    self.is_pawn_here(horse_dict1.get(x) + i,
                                                      board)) < 100 and pawn.texture > 100):
                                    pos.append(horse_dict1.get(x) + i)
                            if self.is_pawn_here(horse_dict2.get(x) + i, board) != False:
                                if (ord(self.is_pawn_here(horse_dict1.get(x) + str(int(i) + 1),
                                                          board)) > 100 and pawn.texture < 100) or (ord(
                                    self.is_pawn_here(horse_dict1.get(x) + str(int(i) + 1),
                                                      board)) < 100 and pawn.texture > 100):
                                    pos.append(horse_dict1.get(x) + str(int(i) + 1))
                            if self.is_pawn_here(horse_dict2.get(x) + i, board) != False:
                                if (ord(self.is_pawn_here(horse_dict1.get(x) + str(int(i) - 1),
                                                          board)) > 100 and pawn.texture < 100) or (ord(
                                    self.is_pawn_here(horse_dict1.get(x) + str(int(i) - 1),
                                                      board)) < 100 and pawn.texture > 100):
                                    pos.append(horse_dict1.get(x) + str(int(i) - 1))
                            if self.is_pawn_here(horse_dict2.get(x) + i, board) != False:
                                if (ord(self.is_pawn_here(horse_dict2.get(x) + str(int(i) - 1),
                                                          board)) > 100 and pawn.texture < 100) or (ord(
                                    self.is_pawn_here(horse_dict2.get(x) + str(int(i) - 1),
                                                      board)) < 100 and pawn.texture > 100):
                                    pos.append(horse_dict2.get(x) + str(int(i) - 1))
                            if self.is_pawn_here(horse_dict2.get(x) + i, board) != False:
                                if (ord(self.is_pawn_here(horse_dict2.get(x) + str(int(i) + 1),
                                                          board)) > 100 and pawn.texture < 100) or (ord(
                                    self.is_pawn_here(horse_dict2.get(x) + str(int(i) + 1),
                                                      board)) < 100 and pawn.texture > 100):
                                    pos.append(horse_dict2.get(x) + str(int(i) + 1))

        print(pos)
        if type == 'move':
            if pawn.texture == 't' and self.is_pawn_here(to, board) == 'k':
                self.insert(pawn, to, board)
                self.insert(self.king1, x + str(int(i) + 1), board)
            elif pawn.texture == 'T' and self.is_pawn_here(to, board) == 'K':
                self.insert(pawn, to, board)
                self.insert(self.king1, x + str(int(i) + 1), board)
            else:
                if to in pos:
                    self.insert(pawn, to, board)
                    self.insert(self.empty, _from, board)
                    return board
                else:
                    print("wrong move")
        elif type == 'check':
            return pos

    def print_board(self, board):
        index = 0
        num = self.data.numbers_row[::-1]
        for x in board:
            print(num[index] + '[', end=" ")
            for y in x:
                if ord(y) > 100:
                    print('\033[94m' + y + '\033[0m', end=" ")
                else:
                    print(y, end=" ")
            print(']')
            index += 1
        print('   A B C D E F G H')

    def is_checkmate(self, which, checks, checks_blue, board2):
        all = []
        pawn_where = 'A1'
        for i in self.data.numbers_vector:
            for z in self.data.numbers_row:
                all.append(i + z)
        print(all)
        if which == 'blue':
            checks_blue_temp = checks_blue.copy()
            for u in all:
                if not 'K' in checks_blue_temp:
                    return False
                if self.is_pawn_here(u, board2) != False:
                    selected_pawn = self.is_pawn_here(u, board2)
                    if selected_pawn == 'P':
                        posible = self.move(self.pawn1, pawn_where, 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.pawn1, selected_pawn, m, board2, 'move')
                    if selected_pawn == 'T':
                        posible = self.move(self.tower1, pawn_where, 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.tower1, selected_pawn, m, board2, 'move')
                    if selected_pawn == 'H':
                        posible = self.move(self.horse1, 'A1', 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.horse1, selected_pawn, m, board2, 'move')
                    if selected_pawn == 'R':
                        posible = self.move(self.runner1, pawn_where, 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.runner1, selected_pawn, m, board2, 'move')
                    if selected_pawn == 'Q':
                        posible = self.move(self.hetman, pawn_where, 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.hetman, selected_pawn, m, board2, 'move')
                    self.pawn11.checks_temp = self.move(self.pawn11, pawn_where, 'A1', board2, 'check')
                    self.tower11.checks_temp = self.move(self.tower11, pawn_where, 'A1', board2, 'check')
                    self.horse11.checks_temp = self.move(self.horse11, pawn_where, 'A1', board2, 'check')
                    self.runner11.checks_temp = self.move(self.runner11, pawn_where, 'A1', board2, 'check')
                    self.hetman1.checks_temp = self.move(self.hetman1, pawn_where, 'A1', board2, 'check')
                    self.king1.checks_temp = self.move(self.king1, pawn_where, 'A1', board2, 'check')
                    if board2 != None:
                        checks_blue_temp = [
                            self.king1.checks_temp,
                            self.runner11.checks_temp,
                            self.tower11.checks_temp,
                            self.horse11.checks_temp,
                            self.hetman.checks_temp,
                            self.pawn11.checks_temp
                        ]
            return True
        if which == 'white':
            checks_temp = checks.copy()
            for u in all:
                if not 'k' in checks_temp:
                    return False
                if self.is_pawn_here(u, board2) != False:
                    selected_pawn = self.is_pawn_here(u, board2)
                    if selected_pawn == 'p':
                        posible = self.move(self.pawn11, pawn_where, 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.pawn11, selected_pawn, m, board2, 'move')
                    if selected_pawn == 't':
                        posible = self.move(self.tower11, pawn_where, 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.tower11, selected_pawn, m, board2, 'move')
                    if selected_pawn == 'h':
                        posible = self.move(self.horse11, pawn_where, 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.horse11, selected_pawn, m, board2, 'move')
                    if selected_pawn == 'r':
                        posible = self.move(self.runner11, pawn_where, 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.runner11, selected_pawn, m, board2, 'move')
                    if selected_pawn == 'q':
                        posible = self.move(self.hetman, pawn_where, 'A1', board2, 'check')
                        for m in posible:
                            board2 = self.move(self.hetman, selected_pawn, m, board2, 'move')
                    self.pawn1.checks_temp = self.move(self.pawn1, pawn_where, 'A1', board2, 'check')
                    self.tower1.checks_temp = self.move(self.tower1, pawn_where, 'A1', board2, 'check')
                    self.horse1.checks_temp = self.move(self.horse1, pawn_where, 'A1', board2, 'check')
                    self.runner1.checks_temp = self.move(self.runner1, pawn_where, 'A1', board2, 'check')
                    self.hetman.checks_temp = self.move(self.hetman, pawn_where, 'A1', board2, 'check')
                    self.king.checks_temp = self.move(self.king, pawn_where, 'A1', board2, 'check')
                    if board2 != None:
                        checks_temp = [
                            self.king1.checks_temp,
                            self.runner11.checks_temp,
                            self.tower11.checks_temp,
                            self.horse11.checks_temp,
                            self.hetman.checks_temp,
                            self.pawn11.checks_temp
                        ]
            return True

    def output(self):
        board1 = [['_' for _ in range(8)] for _ in range(8)]
        board1 = self.insert(self.horse1, self.horse1.location, board1)
        board1 = self.insert(self.horse1, 'G1', board1)
        board1 = self.insert(self.tower1, self.tower1.location, board1)
        board1 = self.insert(self.tower1, 'H1', board1)
        board1 = self.insert(self.runner1, self.runner1.location, board1)
        board1 = self.insert(self.runner1, 'F1', board1)
        board1 = self.insert(self.hetman, self.hetman.location, board1)
        board1 = self.insert(self.king, self.king.location, board1)
        pawns_loc = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2']
        for z in pawns_loc:
            board1 = self.insert(self.pawn1, z, board1)
        board1 = board1[::-1]
        board1 = self.insert(self.horse11, self.horse1.location, board1)
        board1 = self.insert(self.horse11, 'B1', board1)
        board1 = self.insert(self.tower11, self.tower1.location, board1)
        board1 = self.insert(self.tower11, 'A1', board1)
        board1 = self.insert(self.runner11, self.runner1.location, board1)
        board1 = self.insert(self.runner11, 'C1', board1)
        board1 = self.insert(self.hetman1, self.hetman.location, board1)
        board1 = self.insert(self.king1, self.king.location, board1)
        pawns_loc = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2']
        for z in pawns_loc:
            board1 = self.insert(self.pawn11, z, board1)
        self.print_board(board1)
        whith = 0
        is_check_blue = False
        is_check = False
        checks = []
        checks_blue = []

        while True:
            try:
                old_board = board1.copy()
            except AttributeError:
                pass
            pawn_select = input('Select pawn(ex. A2): ')
            selected_pawn = self.is_pawn_here(pawn_select, board1)
            if selected_pawn != False:
                print('You want to move ' + selected_pawn)
                pawn_where = input('Where you want to move?(ex. A3): ')
                if selected_pawn == 'P':
                    board1 = self.move(self.pawn1, pawn_select, pawn_where, board1, 'move')
                    self.pawn1.checks = self.move(self.pawn1, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'T':
                    board1 = self.move(self.tower1, pawn_select, pawn_where, board1, 'move')
                    self.tower1.checks = self.move(self.tower1, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'H':
                    board1 = self.move(self.horse1, pawn_select, pawn_where, board1, 'move')
                    self.horse1.checks = self.move(self.horse1, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'R':
                    board1 = self.move(self.runner1, pawn_select, pawn_where, board1, 'move')
                    self.runner1.checks = self.move(self.runner1, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'Q':
                    board1 = self.move(self.hetman, pawn_select, pawn_where, board1, 'move')
                    self.hetman.checks = self.move(self.hetman, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'K':
                    board1 = self.move(self.king, pawn_select, pawn_where, board1, 'move')
                    self.king.checks = self.move(self.king, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'p':
                    board1 = self.move(self.pawn11, pawn_select, pawn_where, board1, 'move')
                    self.pawn11.checks = self.move(self.pawn11, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 't':
                    board1 = self.move(self.tower11, pawn_select, pawn_where, board1, 'move')
                    self.tower11.checks = self.move(self.tower11, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'h':
                    board1 = self.move(self.horse11, pawn_select, pawn_where, board1, 'move')
                    self.horse11.checks = self.move(self.horse11, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'r':
                    board1 = self.move(self.runner11, pawn_select, pawn_where, board1, 'move')
                    self.runner11.checks = self.move(self.runner11, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'q':
                    board1 = self.move(self.hetman1, pawn_select, pawn_where, board1, 'move')
                    self.hetman1.checks = self.move(self.hetman1, pawn_where, 'A1', board1, 'check')
                if selected_pawn == 'k':
                    board1 = self.move(self.king1, pawn_select, pawn_where, board1, 'move')
                    self.king1.checks = self.move(self.king, pawn_where, 'A1', board1, 'check')
                if board1 != None:
                    checks = [
                        self.king.checks,
                        self.horse1.checks,
                        self.hetman.checks,
                        self.tower1.checks,
                        self.runner1.checks,
                        self.pawn1.checks
                    ]
                    checks_blue = [
                        self.king1.checks,
                        self.runner11.checks,
                        self.tower11.checks,
                        self.horse11.checks,
                        self.hetman.checks,
                        self.pawn11.checks
                    ]
                    for z in checks:
                        for u in z:
                            if self.is_pawn_here(u, board1) == 'k':
                                is_check = True
                    for z in checks_blue:
                        for u in z:
                            if self.is_pawn_here(u, board1) == 'K':
                                is_check_blue = True
                    if is_check and self.is_checkmate('white', checks, checks_blue, board1):
                        return True
                    if is_check_blue and self.is_checkmate('blue', checks, checks_blue, board1):
                        return True
                    if is_check and ord(selected_pawn) > 100:
                        print('wrong move, there is check')
                        self.print_board(old_board)
                        board1 = old_board.copy()
                    elif is_check_blue and ord(selected_pawn) < 100:
                        print('wrong move, there is check')
                        self.print_board(old_board)
                        board1 = old_board.copy()
                    else:
                        self.print_board(board1)
            else:
                print('Brak pionka w ' + pawn_select)


szachownica = board()

if szachownica.output():
    print('koniec gry')

