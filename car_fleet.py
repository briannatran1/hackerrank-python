class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''req:
            - fn takes in 2 int arrs
            - return num of fleet cars that will arrive (int)
            - one-lane road
            - all cars traveling in same direction toward target
            - cars can never pass another car (faster will travel behind and match
            slower car's speed)
            - fleet = cars driving at same speed and same position

            - Sorting by Position: By processing the cars from the closest to the target, 
            we can easily determine when a new fleet is formed because any car behind 
            (with a greater distance from the target) will either join the fleet or 
            form a new one based on its speed and the time it takes to reach the target.
        '''
        # create arr of pairs
        # initialize fleets and curr_time to 0
        # a car's position is always < than target at the start, 
        # so it's fine to start curtime at 0 (no fleet will be at target at time 0)
        # iterate through dist, speed in sorted pairs in reverse
        # calculate time to reach target
        # if curr_time < destination_time, car cannot catch up to fleet so must form new one
        # therefore, increment fleets and set curr_time to arrival time of new fleet
        pairs = zip(position, speed)
        fleets = curr_time = 0  
        
        for dist, speed in sorted(pairs, reverse=True):
            destination_time = (target - dist) / speed
            if curr_time < destination_time:
                fleets += 1
                curr_time = destination_time

        return fleets
