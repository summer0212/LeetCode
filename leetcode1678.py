class Solution:
    def interpret(self, command) :
        str = ""

        for i in range(len(command)):
            if command[i] == "G":
                str += "G"
            elif command[i : i+2] == "()":
                str += "o"
            elif command[i : i+4] == "(al)":
                str += "al"
        return str

        # mp = {
        #     "G" : "G",
        #     "()" : "o",
        #     "(al)" : "al"
        # }
        # output = ""
        # for i in range(0,len(command)):
        #     if command[i] in mp:
        #         output += mp[command[i]]
        #     elif command[i : i+2] in mp:
        #         output += mp[command[i : i+2]]
        #     elif command[i : i + 4] in mp:
        #         output += mp[command[i : i + 4]]
        # return output

    
object = Solution()
print(object.interpret( "(al)G()()()()"))

        