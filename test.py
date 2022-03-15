import unittest
import time
from height_pair import my_solution


class TestHeightPair(unittest.TestCase):

    def bruteForceMethod(self, h_sum, p_list):
        """ implements the pair search standard algorithm O(n2), in order to compare results with the optimized solution """
        start = time.time()
        arr_size = len(p_list)
        final_pairs = set()
        for i in range(0, arr_size - 1):
            for j in range(i + 1, arr_size):
                if int(p_list[i]['h_in']) + int(p_list[j]['h_in']) == h_sum:
                    final_pairs.add((i, j))

        end = time.time()
        print(f"Brute Force Method: total number of pairs = {len(final_pairs)}, time of execution = {end - start}")

        return final_pairs

    def test_get_data(self):
        self.assertIsNotNone(my_solution.getData())

    def test_sort_data(self):
        values = [
            {
                'first_name': 'Alex',
                'h_in': '77',
                'h_meters': '1.96',
                'last_name': 'Acker'
            },
            {
                'first_name': 'Hassan',
                'h_in': '76',
                'h_meters': '1.93',
                'last_name': 'Adams'
            },
            {
                'first_name': 'Arron',
                'h_in': '75',
                'h_meters': '1.96',
                'last_name': 'Afflalo'
            }
        ]
        sorted = my_solution.sortData(values)
        compared = [
            {
                'first_name': 'Arron',
                'h_in': '75',
                'h_meters': '1.96',
                'last_name': 'Afflalo'
            },
            {
                'first_name': 'Hassan',
                'h_in': '76',
                'h_meters': '1.93',
                'last_name': 'Adams'
            },
            {
                'first_name': 'Alex',
                'h_in': '77',
                'h_meters': '1.96',
                'last_name': 'Acker'
            }
        ]

        self.assertEqual(sorted, compared, 'Should be the same array')

    def test_pairs_find(self):
        values = [
            {
                'first_name': 'Alex',
                'h_in': '77',
                'h_meters': '1.96',
                'last_name': 'Acker'
            },
            {
                'first_name': 'Hassan',
                'h_in': '76',
                'h_meters': '1.93',
                'last_name': 'Adams'
            },
            {
                'first_name': 'Arron',
                'h_in': '75',
                'h_meters': '1.96',
                'last_name': 'Afflalo'
            },
                        {
                'first_name': 'Mike',
                'h_in': '75',
                'h_meters': '1.80',
                'last_name': 'Smith'
            }

        ]
        sorted = my_solution.sortData(values)

        pairs = my_solution.find_pairs(153, sorted)
        self.assertEqual(len(pairs), 1, 'Size match')
        pairs = my_solution.find_pairs(152, sorted)
        self.assertEqual(len(pairs), 2, 'Size match')
        pairs = my_solution.find_pairs(200, sorted)
        self.assertEqual(len(pairs), 0, 'Size match')


    def test_brute_vs_optimized_methods(self):

        players_list = my_solution.getData()
        sorted_list = my_solution.sortData(players_list)

        brute_force_pairs = self.bruteForceMethod(161, sorted_list)
        opt_pairs = my_solution.find_pairs(161, sorted_list)
        self.assertEqual(brute_force_pairs, opt_pairs, 'Sets are equal')

