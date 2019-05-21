"""
This problem was asked by Stripe.
Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.
It should contain the following methods:
•	set(key, value, time): sets key to value for t = time.
•	get(key, time): gets the key at t = time.
The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time.
In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.
Consider the following examples:
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
"""

import bisect


class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key, value, time):
        """
        Sets key to value for t = time.
        Time: O(n) where n is number of values key takes.
        Space: O(n)
        """
        if key not in self.data:
            self.data[key] = [(time, value)]
        else:
            # Overwrite value and time
            self.data[key] = [(t, v) for (t, v) in self.data[key]
                              if value != v and time != t]
            # Inserts data in sorted order
            bisect.insort_left(self.data[key], (time, value))

    def get(self, key, time):
        """
        Gets value of key at t = time.
        Time: O(log n) where n is number of values key takes
        Space: O(1) (no values stored or modified)
        """
        # Key not found
        if key not in self.data:
            return

        # Return value if times are equal (checks case when idx = 0)
        t, v = self.data[key][0]
        if time == t:
            return v

        # Returns index where time should be inserted
        # to maintain sorted order
        idx = bisect.bisect_left(self.data[key], (time, ))

        # Time comes after earliest recorded time
        # Return value occuring at or before idx
        if idx:
            _, v = self.data[key][idx-1]
            return v
        # None returned if time < earliest t


if __name__ == "__main__":
    d = TimeMap()
    d.set(1, 1, 0)  # set key 1 to value 1 at time 0
    d.set(1, 2, 2)  # set key 1 to value 2 at time 2
    print(d.get(1, 1))  # get key 1 at time 1 should be 1
    print(d.get(1, 3))  # get key 1 at time 3 should be 2
    d.set(1, 1, 5)  # set key 1 to value 1 at time 5
    print(d.get(1, 0))  # get key 1 at time 0 should be null
    print(d.get(1, 10))  # get key 1 at time 10 should be 1
    d.set(1, 1, 0)  # set key 1 to value 1 at time 0
    d.set(1, 2, 0)  # set key 1 to value 2 at time 0
    print(d.get(1, 0))  # get key 1 at time 0 should be 2
    print(d.get(1, -1))
    print(d.get(1, 20))
