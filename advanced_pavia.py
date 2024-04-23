'''Python: Advanced

70 points

This assignment will develop your ability to manipulate data.
We expect that this assignment will equip you to understand
    Python tutorials.

Please refer to the file `advanced_sample_data.py` for examples of:
- the `social_graph` parameter for the relationship_status item
- the `board` parameter for the tic_tac_toe item
- the `route_map` parameter for the eta item
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see `advanced_sample_data.py` for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from advanced_sample_data import social_graph # type: ignore

    to_followers = social_graph[to_member]['following']
    from_followers = social_graph[from_member]['following']

    index_n = 0

    def forward_rel(from_list):
        index = 0
        for n in from_list:
            user = to_followers[index]
            #print(user)
            if user == from_member:
                return True
            else:
                index = index + 1

        return False
    
    def backward_rel(to_list):
        index = 0
        for n in (to_list):
            user = from_followers[index]
            #print(user)
            if user == to_member:
                return True
            else:
                index = index + 1

        return False
    
    #print(forward_rel(to_followers))
    #print(backward_rel(to_followers))

    if (forward_rel(to_followers)) == True and (backward_rel(from_followers)) == True:
        print("friends")
    elif (forward_rel(to_followers)) == False and (backward_rel(from_followers)) == True:
        print("followed by")
    elif (forward_rel(to_followers)) == True and (backward_rel(from_followers)) == False:
        print("follows")
    else:
        print("no relationship")

relationship_status('@eeebeee', '@chums','friends')

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see `advanced_sample_data.py` for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner, or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    win_result = "NO WINNER"
    xwinner = ['X', 'X', 'X']
    owinner = ['O', 'O', 'O']
    # Write a function for each win condition

    # Win condition 1: horizontal win
    def horizontal_win(check_board):
        
        for r in range(len(check_board)):
            if check_board[r] == xwinner:
                print('X')
            elif check_board[r] == owinner:
                print('O')

        return win_result

    # Win condition 2: vertical win
    def vertical_win(check_board):
        
        column_num = 0

        while column_num < 3:
            
            index_check = []
        
            for r in range(len(check_board)):
                index_check.append(check_board[r][column_num])
            
            if index_check == xwinner:
                print('X')
            elif index_check == owinner:
                print('O')
            
            column_num = column_num + 1

        return win_result

    # Win condition 3: diagonal win
    def diagonal_win(check_board):
        
        row_num = 1
        column_num = 1

        for n in range(len(check_board)):
        
            # check the 3 x 3's they're easy

            if check_board[row_num][column_num] == check_board[row_num - 1][column_num - 1]:
                
                if check_board[row_num + 1][column_num + 1] and check_board[row_num][column_num] == 'X':
                    print('X')
                    return win_result
                
                elif check_board[row_num + 1][column_num + 1] and check_board[row_num][column_num] == 'O':
                    print('O')
                    return win_result
                
                else:
                    row_num = row_num + 1
                    column_num = column_num + 1

        print(win_result)
        return win_result
    
    horizontal_win(board)
    vertical_win(board)
    diagonal_win(board)

from advanced_sample_data import board1 # type: ignore
from advanced_sample_data import board2 # type: ignore
from advanced_sample_data import board3 # type: ignore
from advanced_sample_data import board4 # type: ignore
from advanced_sample_data import board5 # type: ignore
from advanced_sample_data import board6 # type: ignore
from advanced_sample_data import board7 # type: ignore

tic_tac_toe(board1) # test here
tic_tac_toe(board2) # test here
tic_tac_toe(board3) # test here
tic_tac_toe(board4) # test here
tic_tac_toe(board5) # test here
tic_tac_toe(board6) # test here
tic_tac_toe(board7) # test here

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see `advanced_sample_data.py` for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    from advanced_sample_data import route_map # type: ignore
    upd_key = 'a1'
    admu_key = 'a2'
    dlsu_key = 'b1'

    #print(route_map)
    #check the route
    
    if first_stop == 'upd' and second_stop == 'admu':
        print(route_map[upd_key, admu_key]['travel_time_mins'])
    elif first_stop == 'admu' and second_stop == 'dlsu':
        print(route_map[admu_key, dlsu_key]['travel_time_mins'])
    elif first_stop == 'dlsu' and second_stop == 'upd':
        print(route_map[dlsu_key,upd_key]['travel_time_mins'])

eta("upd", "admu", "a1")