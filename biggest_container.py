class Solution():
    def maxArea_1(self, height):
            # we find all the combinations of two entries in the list and  store them as tuples , O(n2)
            # iterate through all those combinations and keep updating the max area counter
            # [find the area using min(x,y)* (j-i) i<j where x and y are two entries in the tuple
        tuple_list = []
        for i, x in enumerate(height):
            for j in range(i+1,len(height)):
                tuple_list.append((x, height[j], i, j)) # x,y,i,j
        _area = []
        for tuple in tuple_list:
            _area.append(min(tuple[0],tuple[1])*(tuple[3]-tuple[2]))
        print(_area)
        return max(_area)

    def maxArea_1_1(self,height):
        _area = 0
        if len(height) in [0, 1]:
            return 0
        for i, x in enumerate(height):
            for j in range(i + 1, len(height)):
                _area = max(_area, min(x, height[j]) * (j - i))
        return _area

    def maxArea_2(self, height):
        # based on window
        # start window and iterate over the array
        # maintain two pointers window_Start and window_last
        # compute area and move the pointer pointing the shortest line to the next index
        # compute and store the maximum of areas in _areas variable
        # perform until window_right-window-left = 1
        window_left = 0
        window_right = len(height)-1
        _area = 0
        if len(height) in [0,1]:
            return 0
        if len(height) == 2:
            return min(height[window_right], height[window_left])*1
        while window_right-window_left != 0:
            _area = max((min(height[window_right], height[window_left]))*(window_right-window_left), _area)
            minimum_height_index = min([window_right, window_left], key=lambda x: height[x])
            if minimum_height_index == window_right:
                window_right -= 1
            if minimum_height_index == window_left:
                window_left += 1
        return _area

lister = [1, 8, 6, 2, 5, 4, 8, 3, 7]
obj = Solution()
y = obj.maxArea_2(lister)
print(y)

