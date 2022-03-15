from urllib.request import urlopen
import json
import time


def getData():
    """fetches JSON data from URL"""
    api_url = "https://mach-eight.uc.r.appspot.com/"
    with urlopen(api_url) as response:
        json_response = json.load(response)
        return json_response['values']

def sortData(data):
    data.sort(key=lambda x: x['h_in'])
    return data

def createHashTable(p_list):
    """Creates a dictionary where the (key, value) pair corresponds to
    ('height', [players_ids with that height value])  """
    hashed_dict = dict()
    size = len(p_list)
    for i in range(size):
        if p_list[i]['h_in'] in hashed_dict:
            hashed_dict[p_list[i]['h_in']].append(i)
        else:
            hashed_dict[p_list[i]['h_in']] = [i]

    return hashed_dict


def find_pairs(h_sum, p_list):
    """ find all pairs of players within a sorted list that the sum of their heights equals a given value sum """
    start = time.time()
    # creates the dictionary with players_ids and height as key
    hashed_players_by_height = createHashTable(p_list)
    final_pairs = set()

    # loops through the dictionary , for each height , the remaining height to reach SUM is calculated
    # and with that difference value as a new key we get the list of players_ids that have that height
    for height, leftIds in hashed_players_by_height.items():
        current_height = int(height)
        diff = h_sum - current_height

        # we only need to get players_ids if their height is greater or equal to the current height
        if diff >= current_height:
            rightIds = hashed_players_by_height.get(str(diff))
            if rightIds is not None:
                # if there are players with the required height then we create all possible pairs, excluding
                # all (i,i) pairs and all (j,i) inverted pairs
                for i in leftIds:
                    for j in rightIds:
                        if i < j:
                            final_pairs.add((i, j))

    end = time.time()
    print(f"Optimized Method: total number of pairs = {len(final_pairs)}, time of execution = {end - start}")

    return final_pairs


def getMinMaxHeightSums(p_list):
    """calculates the minimum and maximum height sum for a sorted list of players"""

    min_s = int(p_list[0]['h_in']) + int(p_list[1]['h_in'])
    max_s = int(p_list[-1]['h_in']) + int(p_list[-2]['h_in'])

    return min_s, max_s


def printPairs(total_pairs, p_list):
    """"Prints all players pairs given a set of players ids and a list of players"""
    if len(total_pairs):
        for ele in total_pairs:
            print(
                f"{p_list[ele[0]]['first_name']} {p_list[ele[0]]['last_name']} ({p_list[ele[0]]['h_in']}) : "
                f"{p_list[ele[1]]['first_name']} {p_list[ele[1]]['last_name']}({p_list[ele[1]]['h_in']})")

    else:
        print(f"No pairs were found!")


# Main
if __name__ == '__main__':

    players = sortData(getData())
    min_sum, max_sum = getMinMaxHeightSums(players)

    x = int(input("Enter SUM of Heights = "))

    if (x <= max_sum) and (x >= min_sum):

        existing_pairs = find_pairs(x, players)
        printPairs(existing_pairs, players)

    else:
        print(f"No pairs were found!")
