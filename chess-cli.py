#!/usr/bin/env python
# -*- coding: utf-8 -*-
class board:
    class pawn:
        def __init__(self, location, texture, move_type, checks, status):
            self.location = location
            self.texture = texture
            self.move_type = move_type
            self.checks = checks
            self.status = status

    tower1 = pawn('A1', 'T', 'tower', '', True)
    horse1 = pawn('B1', 'H', 'horse', '', True)
    runner1 = pawn('C1', 'R', 'runner', '', True)
    hetman = pawn('D1', 'Q', 'hetman', '', True)
    king = pawn('E1', 'K', 'king', '', True)
    pawn1 = pawn('A2', 'P', 'pawn', '', True)
    empty = pawn('none', '_', 'none', '', True)
    tower11 = pawn('A8', 't', 'tower', '', True)
    horse11 = pawn('B8', 'h', 'horse', '', True)
    runner11 = pawn('C8', 'r', 'runner', '', True)
    hetman1 = pawn('D8', 'q', 'hetman', '', True)
    king1 = pawn('E8', 'k', 'king', '', True)
    pawn11 = pawn('A7', 'p', 'pawn', '', True)

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
        roszade = False
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
                                if horse_dict1.get(x) != None and self.is_pawn_here(horse_dict1.get(x) + str(int(i) - 1), board) != False:
                                    pos.append(horse_dict1.get(x) + str(int(i) - 1))
                                if horse_dict2.get(x) != None and self.is_pawn_here(horse_dict2.get(x) + str(int(i) - 1), board) != False:
                                    pos.append(horse_dict2.get(x) + str(int(i) - 1))
                            else:
                                if i == '2':
                                    pos.append(x + str(int(i) + 2))
                                if self.is_pawn_here(x + str(int(i) + 1), board) == False:
                                    pos.append(x + str(int(i) + 1))
                                if horse_dict1.get(x) != None and self.is_pawn_here(horse_dict1.get(x) + str(int(i) + 1), board) != False:
                                    pos.append(horse_dict1.get(x) + str(int(i) + 1))
                                if horse_dict2.get(x) != None and self.is_pawn_here(horse_dict2.get(x) + str(int(i) + 1), board) != False:
                                    pos.append(horse_dict2.get(x) + str(int(i) + 1))
                        if pawn.move_type == 'tower':
                            lock_up = False
                            lock_row = False
                            for a in range(1, 7):
                                    if not lock_up:
                                        pos.append(x + str(int(i) + a))
                                        if self.is_pawn_here(x + str(int(i) + a), board) != False and self.is_pawn_here(x + str(int(i) + a), board) != pawn.texture:
                                            lock_up = True
                            for m in self.data.numbers_vector:
                                if not lock_row:
                                    pos.append(m + i)
                                    if self.is_pawn_here(m + i, board) != False and self.is_pawn_here(m + i, board) != pawn.texture:
                                        lock_row = True
                        if pawn.move_type == 'horse':
                            if horse_dict1.get(x) != None:
                                pos.append(horse_dict1.get(x) + str(int(i) + 2))
                                pos.append(horse_dict1.get(x) + str(int(i) - 2))
                            if horse_dict2.get(x) != None:
                                pos.append(horse_dict2.get(x) + str(int(i) + 2))
                                pos.append(horse_dict2.get(x) + str(int(i) - 2))
                            if horse_dict3.get(x) != None:
                                pos.append(horse_dict3.get(x) + str(int(i) + 1))
                                pos.append(horse_dict3.get(x) + str(int(i) - 1))
                            if horse_dict4.get(x) != None:
                                pos.append(horse_dict4.get(x) + str(int(i) + 1))
                                pos.append(horse_dict4.get(x) + str(int(i) - 1))

                        if pawn.move_type == 'runner':
                            u = x
                            lock = False
                            z = 1
                            c = 0
                            while not lock and c < 8:
                                if horse_dict1.get(u) != None:
                                    pos.append(horse_dict1.get(u) + str(int(i) + z))
                                    if self.is_pawn_here(horse_dict1.get(u) + str(int(i) + z), board) != False:
                                        lock = True
                                c += 1
                                u = horse_dict1.get(u)
                                z += 1
                            lock = False
                            u = x
                            z = 1
                            c = 0
                            while not lock and c < 8:
                                if horse_dict1.get(u) != None:
                                    pos.append(horse_dict1.get(u) + str(int(i) - z))
                                    if self.is_pawn_here(horse_dict1.get(u) + str(int(i) - z), board) != False:
                                        lock = True
                                c += 1
                                u = horse_dict1.get(u)
                                z += 1
                            lock = False
                            u = x
                            c = 0
                            z = 1
                            while not lock and c < 8:
                                if horse_dict2.get(u) != None:
                                    pos.append(horse_dict2.get(u) + str(int(i) + z))
                                    if self.is_pawn_here(horse_dict2.get(u) + str(int(i) + z), board) != False:
                                        lock = True
                                c += 1
                                u = horse_dict2.get(u)
                                z += 1
                            lock = False
                            u = x
                            z = 1
                            c = 0
                            while not lock and c < 8:
                                if horse_dict2.get(u) != None:
                                    pos.append(horse_dict2.get(u) + str(int(i) - z))
                                    if self.is_pawn_here(horse_dict2.get(u) + str(int(i) - z), board) != False:
                                        lock = True
                                c += 1
                                u = horse_dict2.get(u)
                                z += 1
                        if pawn.move_type == 'hetman':
                            lock_up = False
                            lock_row = False
                            for a in range(1, 7):
                                    if not lock_up:
                                        pos.append(x + str(int(i) + a))
                                        if self.is_pawn_here(x + str(int(i) + a), board) != False and self.is_pawn_here(x + str(int(i) + a), board) != pawn.texture:
                                            lock_up = True
                            for m in self.data.numbers_vector:
                                if not lock_row:
                                    pos.append(m + i)
                                    if self.is_pawn_here(m + i, board) != False and self.is_pawn_here(m + i, board) != pawn.texture:
                                            lock_row = True
                            u = x
                            lock = False
                            z = 1
                            c = 0
                            while not lock and c < 8:
                                if horse_dict1.get(u) != None:
                                    pos.append(horse_dict1.get(u) + str(int(i) + z))
                                    if self.is_pawn_here(horse_dict1.get(u) + str(int(i) + z), board) != False:
                                        lock = True
                                c += 1
                                u = horse_dict1.get(u)
                                z += 1
                            lock = False
                            u = x
                            z = 1
                            c = 0
                            while not lock and c < 8:
                                if horse_dict1.get(u) != None:
                                    pos.append(horse_dict1.get(u) + str(int(i) - z))
                                    if self.is_pawn_here(horse_dict1.get(u) + str(int(i) - z), board) != False:
                                        lock = True
                                c += 1
                                u = horse_dict1.get(u)
                                z += 1
                            lock = False
                            u = x
                            c = 0
                            z = 1
                            while not lock and c < 8:
                                if horse_dict2.get(u) != None:
                                    pos.append(horse_dict2.get(u) + str(int(i) + z))
                                    if self.is_pawn_here(horse_dict2.get(u) + str(int(i) + z), board) != False:
                                        lock = True
                                c += 1
                                u = horse_dict2.get(u)
                                z += 1
                            lock = False
                            u = x
                            z = 1
                            c = 0
                            while not lock and c < 8:
                                if horse_dict2.get(u) != None:
                                    pos.append(horse_dict2.get(u) + str(int(i) - z))
                                    if self.is_pawn_here(horse_dict2.get(u) + str(int(i) - z), board) != False:
                                        lock = True
                                c += 1
                                u = horse_dict2.get(u)
                                z += 1
                        if pawn.move_type == 'king':
                            pos.append(x + str(int(i) + 1))
                            pos.append(x + str(int(i) - 1))
                            if horse_dict1.get(x) != None:
                                pos.append(horse_dict1.get(x) + i)
                                pos.append(horse_dict1.get(x) + str(int(i) + 1))
                                pos.append(horse_dict1.get(x) + str(int(i) - 1))
                            if horse_dict2.get(x) != None:
                                pos.append(horse_dict2.get(x) + str(int(i) - 1))
                                pos.append(horse_dict2.get(x) + str(int(i) + 1))
                                pos.append(horse_dict2.get(x) + i)

                            if (_from == 'E1' and self.is_pawn_here('H1', board) == 't') or (_from == 'E8' and self.is_pawn_here('H8', board) == 'T'):
                                roszade = True

        for n in pos:
            if self.is_pawn_here(n, board) != False:
                    try:
                        if (ord(self.is_pawn_here(n, board)) > 100 and ord(pawn.texture) > 100) or (ord(self.is_pawn_here(n, board)) < 100 and ord(pawn.texture) < 100):
                            pos.remove(n)
                    except TypeError:
                        pass

        for y in pos:
            if '0' in y:
                pos.remove(y)
            elif '-' in y:
                pos.remove(y)
        #print(pos)
        textures = {
            'k':self.king1, 't': self.tower11, 'h':self.horse11, 'q':self.hetman1, 'r':self.runner11, 'p':self.pawn11,
            'K':self.king, 'T': self.tower1, 'H':self.horse1, 'Q':self.hetman, 'R':self.runner1, 'P':self.pawn
        }
        if type == 'move':
            if roszade == True and to == 'G1':
                if pawn.texture == 'k':
                    self.insert(self.king1, 'G1', board)
                    self.insert(self.empty, _from, board)
                    self.insert(self.tower11, 'F1', board)
                    self.insert(self.empty, 'H1', board)
                else:
                    self.insert(self.king, 'G8', board)
                    self.insert(self.empty, _from, board)
                    self.insert(self.tower1, 'F8', board)
                    self.insert(self.empty, 'H8', board)

            if to in pos:
                if '8' in to and pawn.texture == 'p':
                    promotion = input('for what you want to change?: ')
                    if promotion == 'q':
                        self.insert(self.hetman1, to, board)
                    if promotion == 'h':
                       self.insert(self.horse11, to, board)
                    if promotion == 'r':
                       self.insert(self.runner11, to, board)
                    if promotion == 't':
                       self.insert(self.tower11, to, board)
                elif '1' in to and pawn.texture == 'P':
                    promotion = input('for what you want to change?: ')
                    if promotion == 'Q':
                       self.insert(self.hetman, to, board)
                    if promotion == 'H':
                       self.insert(self.horse1, to, board)
                    if promotion == 'R':
                       self.insert(self.runner1, to, board)
                    if promotion == 'T':
                       self.insert(self.tower1, to, board)
                else:
                    if self.is_pawn_here(to, board) != False:
                        destroyed_pawn = self.is_pawn_here(to, board)
                        print('zbito ' + destroyed_pawn)
                        obj = textures.get(destroyed_pawn)
                        obj.status = False
                    self.insert(pawn, to, board)
                    self.insert(self.empty, _from, board)
            else:
                    print("wrong move")
            return board
        elif type == 'check':
            if pawn.texture == 'k' and roszade == True:
                pos.append('G1')
            elif pawn.texture == 'K' and roszade == True:
                pos.append('')
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


    def boardcopy(self, board):
        new = [[] for _ in range(8)]
        for q in range(len(board)):
            m = board[q]
            for x in m:
                new[q].append(x)

        return new

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
        need_refresh_white = False
        need_refresh_blue = False
        while True:
            old_board = self.boardcopy(board1)
            pawn_select = input('Select pawn(eg. A2): ')
            selected_pawn = self.is_pawn_here(pawn_select, board1)
            if selected_pawn != False:
                movements = {
                    'p': self.move(self.pawn11, pawn_select, 'A1', board1, 'check'),
                    't': self.move(self.tower11, pawn_select, 'A1', board1, 'check'),
                    'q': self.move(self.hetman1, pawn_select, 'A1', board1, 'check'),
                    'k': self.move(self.king1, pawn_select,'A1', board1, 'check'),
                    'h': self.move(self.horse11, pawn_select, 'A1', board1, 'check'),
                    'r': self.move(self.runner11, pawn_select, 'A1', board1, 'check'),
                    'P': self.move(self.pawn1, pawn_select, 'A1', board1, 'check'),
                    'T': self.move(self.tower1, pawn_select, 'A1', board1, 'check'),
                    'Q': self.move(self.hetman, pawn_select, 'A1', board1, 'check'),
                    'K': self.move(self.king, pawn_select, 'A1', board1, 'check'),
                    'H': self.move(self.horse1, pawn_select, 'A1', board1, 'check'),
                    'R': self.move(self.runner1, pawn_select, 'A1', board1, 'check')
                }
                print('You want to move ' + selected_pawn)
                print('Possible moves are: ')
                for q in movements.get(selected_pawn):
                    print(q)
                pawn_where = input('Where you want to move?(eg. A3): ')
                if selected_pawn == 'P':
                    board1 = self.move(self.pawn1, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'T':
                    board1 = self.move(self.tower1, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'H':
                    board1 = self.move(self.horse1, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'R':
                    board1 = self.move(self.runner1, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'Q':
                    board1 = self.move(self.hetman, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'K':
                    board1 = self.move(self.king, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'p':
                    board1 = self.move(self.pawn11, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 't':
                    board1 = self.move(self.tower11, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'h':
                    board1 = self.move(self.horse11, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'r':
                    board1 = self.move(self.runner11, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'q':
                    board1 = self.move(self.hetman1, pawn_select, pawn_where, board1, 'move')
                if selected_pawn == 'k':
                    board1 = self.move(self.king1, pawn_select, pawn_where, board1, 'move')
                if board1 != None:
                    if self.pawn11.status:
                        self.pawn11.checks = self.move(self.pawn11, pawn_where, 'A1', board1, 'check')
                    else:
                        self.pawn11.checks = ''
                    if self.pawn11.status:
                        self.tower11.checks = self.move(self.tower11, pawn_where, 'A1', board1, 'check')
                    else:
                        self.tower11.checks = ''
                    if self.horse11.status:
                        self.horse11.checks = self.move(self.horse11, pawn_where, 'A1', board1, 'check')
                    else:
                        self.horse11.checks = ''
                    if self.runner11.status:
                        self.runner11.checks = self.move(self.runner11, pawn_where, 'A1', board1, 'check')
                    else:
                        self.runner11.checks = ''
                    if self.hetman1.status:
                        self.hetman1.checks = self.move(self.hetman1, pawn_where, 'A1', board1, 'check')
                    else:
                        self.hetman1.checks = ''
                    if self.king1.status:
                        self.king1.checks = self.move(self.king1, pawn_where, 'A1', board1, 'check')
                    else:
                        self.king1.checks = ''
                    if self.pawn1.status:
                        self.pawn1.checks = self.move(self.pawn1, pawn_where, 'A1', board1, 'check')
                    else:
                        self.pawn1.checks = ''
                    if self.tower1.status:
                        self.tower1.checks = self.move(self.tower1, pawn_where, 'A1', board1, 'check')
                    else:
                        self.tower1.checks = ''
                    if self.horse1.status:
                        self.horse1.checks = self.move(self.horse1, pawn_where, 'A1', board1, 'check')
                    else:
                        self.horse1.checks = ''
                    if self.runner1.status:
                        self.runner1.checks = self.move(self.runner1, pawn_where, 'A1', board1, 'check')
                    else:
                        self.runner1.checks = ''
                    if self.hetman.status:
                        self.hetman.checks = self.move(self.hetman, pawn_where, 'A1', board1, 'check')
                    else:
                        self.hetman.checks = ''
                    if self.king.status:
                        self.king.checks = self.move(self.king, pawn_where, 'A1', board1, 'check')
                    else:
                        self.king.checks = ''

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
                        self.hetman1.checks,
                        self.pawn11.checks
                        ]
                    print(checks_blue)
                    for z in checks:
                        for u in z:
                            if self.is_pawn_here(u, board1) == 'k':
                                is_check = True
                                need_refresh_white = True
                    for z in checks_blue:
                        for u in z:
                            if self.is_pawn_here(u, board1) == 'K':
                                is_check_blue = True
                                need_refresh_blue = True
                    if is_check and ord(selected_pawn) > 100:
                        print('wrong move, your opponent have check')
                        board1 = self.boardcopy(old_board)
                        self.print_board(board1)
                    elif is_check_blue and ord(selected_pawn) < 100:
                        print('wrong move, your opponent have check')
                        board1 = self.boardcopy(old_board)
                        self.print_board(board1)
                    else:
                        self.print_board(board1)
                else:
                    board1 = []
                    for q in old_board:
                        board1.append(q)
            else:
                print('No pawn in ' + pawn_select)


szachownica = board()

if szachownica.output():
    print('end of the game')
