class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        # Step 1: Calculate the degree of each city
        degree = defaultdict(int)
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        
        # Step 2: Sort cities based on degree
        sorted_cities = sorted(degree.keys(), key=lambda x: degree[x], reverse=True)
        
        # Step 3: Assign values from n to 1 based on sorted order
        city_value = {}
        value = n
        for city in sorted_cities:
            city_value[city] = value
            value -= 1
        
        # Step 4: Calculate the total importance
        total_importance = 0
        for road in roads:
            total_importance += city_value[road[0]] + city_value[road[1]]
        
        return total_importance