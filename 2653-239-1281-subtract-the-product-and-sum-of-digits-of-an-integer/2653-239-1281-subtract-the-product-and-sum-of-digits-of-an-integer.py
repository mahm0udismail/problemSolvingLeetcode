class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        x= str(n)
        product_of_digits = 1  
        Sum_of_digits = 0  
        for i in range(len(x)):
            product_of_digits = product_of_digits * int(x[i])
            Sum_of_digits = Sum_of_digits + int(x[i])
        
        return product_of_digits - Sum_of_digits
        