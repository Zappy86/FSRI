from math import comb

class GraphPebbling:
    '''Class to represent one distribution of a pebbling graph with utility functions. m is the 
    number of vertices on one side of the graph, n is the number of vertices on the other side. 
    m must be greater than or equal to n.'''

    m = 0
    n = 0
    graph = []

    def __init__(self, m, n):
        self.change_m_and_n(m, n)

    def change_m_and_n(self, m, n):
        if m < n:
            raise ValueError("m must be greater than or equal to n")
        
        self.m = m
        self.n = n

    def check_reachability(self, target_side, target_index, t):
        # The number of pebbles on the target vertex
        target_total = self.graph[target_side][target_index]

        # print(f"Target total: {target_total}")

        temp = self.graph[target_side].copy()
        temp.pop(target_index)

        # On the same side as the target vertex, it rounds the number of pebbles on each vertex
        # down to the nearest even number and then sums them up.
        same_side_even_total = sum([(x // 2) * 2 for x in temp])

        # print(f"Same side even total: {same_side_even_total}")

        # Sets opposite_side to the other side of the graph
        opposite_side = self.graph[int(not target_side)].copy()

        # print(f"Opposite side: {opposite_side}")

        # number of vertices with odd amounts on the opposite side of the graph
        num_of_odds = 0

        # For each vertex on the opposite side of the graph, it adds half of the number of pebbles rounded down
        # to the target vertex, and counts the number of vertices with odd amounts of pebbles.
        for i in opposite_side:
            if i % 2 == 1:
                num_of_odds += 1

            target_total += i // 2

        # print(f"Target total after opposite side: {target_total}")
        # print(f"Number of odds on opposite side: {num_of_odds}")

        # moves pebbles from the same side of the graph to the target vertex using the ones left over from the
        # previous step, i.e. the number of vertices wiith odd amounts of pebbles
        for i in range(num_of_odds):
            if same_side_even_total < 2:
                break
            same_side_even_total -= 2
            target_total += 1

        # print(f"Target total after same side with odds on opposite: {target_total}")

        # moves pebbles from the same side of the graph to the target vertex given that there are
        # none left on the opposite side of the graph
        target_total += same_side_even_total // 4

        # print(f"Target total after none on opposite side: {target_total}")

        if target_total < t:
            return False
        else:
            return True

    # thanks chatgpt for this one
    def distributions(self, k, j):
        """Yield every distribution of k elements among j bins."""
        if j == 1:
            yield [k]
            return
    
        for i in range(k + 1):
            for rest in self.distributions(k - i, j - 1):
                yield [i] + rest
    
    def check_every_distribution(self, lower_bound, upper_bound, t):
        progress = 0
        valid_distributions = {}

        # number of vertices/bins
        j = self.m + self.n

        # checks every distribution of k pebbles among j vertices/bins, 
        # where k is between lower_bound and upper_bound
        for k in range(lower_bound, upper_bound + 1):
            for distribution in self.distributions(k, j):
                if progress % 10000 == 0:
                    print(f"Progress: {progress/comb(k + j - 1, j - 1):.2%} through k={k}", end="\r")
                progress += 1
                # print(f"\nChecking distribution: {distribution}")
                self.graph = [distribution[0:self.m], distribution[self.m:]]

                flag = True
                for i in range(j):
                    # print(f"Checking reachability for vertex {i}")
                    if not self.check_reachability(i >= self.m, i % self.m, t):
                        flag = False
                        break
                    
                if flag:
                    if k not in valid_distributions:
                        valid_distributions[k] = [distribution]
                    else:
                        valid_distributions[k] = valid_distributions[k] + [distribution]
            progress = 0
        return valid_distributions

if __name__ == "__main__":
    from pprint import pprint

    m = 4
    n = 4
    lower_bound = 47
    upper_bound = 48
    t = 22

    graph_pebbling = GraphPebbling(m, n)

    valid_distributions = graph_pebbling.check_every_distribution(lower_bound, upper_bound, t)

    pprint(valid_distributions)
    print(valid_distributions.keys())