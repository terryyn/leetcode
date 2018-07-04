class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        first_flag = True
        index = 0
        cur = 0
        cur_index = 0
        result = 0
        while index < len(height):
            #omit the starting 0s 
            if height[index] == 0 and first_flag:
                index+=1
                continue
                
            elif height[index] != 0 and index != len(height)-1:
                first_flag = False
                i = index+1
                while i < len(height):
                    
                    if height[i]>= height[index]:
                        #when encounter a higher height, all space in the middle will be trapped 
                        for j in range(index,i):
                            result += height[index]-height[j]
                        cur = 0
                        break
                        
                    else:
                        if height[i]>cur:
                            cur = height[i]
                            cur_index = i
                    i+=1
                    
                if i == len(height):
                    #the situation where the current index is the highest, so go to the highest height after that
                    if cur_index > index:

                        for j in range(index+1,cur_index):
                            result += (cur-height[j])
                        index = cur_index
                        cur = 0
                    else:
                        index+=1
                else:
                    index = i
            else:
                index+=1
        return result
