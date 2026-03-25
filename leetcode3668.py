class Solution:
    def recoverOrder(self, order, friends) :
        '''
        Wrong statement:
            output[len(friends)] = []
        '''
        output = [None] * len(friends)
        index_val = 0


        '''The Wrong way is below'''

        # for i in range(0, len(friends)):
        #     index_val = order.index(friends[i])
        #     print(index_val)
        #     '''
        #     output[index_val] = friends[i] --> ERROR
        #     The error occurs because index_val (from order) can exceed len(friends). For example, order = [3,1,2,5,4] and friends = [1,3,4] means order.index(4) is 4, but output has length 3.
        #     '''
        #     output[index_val - 1] = friends[i]
        # print(output)

        output = []

        for i in range(0,len(order) ):
            if order[i] in friends:
                output.append(order[i])

        return output


object = Solution()
print(object.recoverOrder(order = [3,1,2,5,4], friends = [1,3,4]))
        