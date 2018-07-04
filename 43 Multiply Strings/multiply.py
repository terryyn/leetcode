class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_reverse = num1[::-1]
        num2_reverse = num2[::-1]
        result = [0]*(len(num1)+len(num2))
        index = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp = int(num1_reverse[i])*int(num2_reverse[j])
                result[i+j] += temp
                result[i+j+1] += result[i+j]//10
                result[i+j] %= 10
        zero_flag = True
        result_string = ""
        for i in range(len(result)-1,-1,-1):
            if result[i] == 0 and zero_flag:
                continue
            elif result[i] !=0 and zero_flag:
                zero_flag = False
            result_string += str(result[i])
        if zero_flag:
            result_string = '0'
        return result_string
