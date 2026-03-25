# from operator import le


class Solution:
    def calPoints(self, operations):
        record = []

        

        for i in range(0,len(operations)):
            # if operations[i].isdigit():
            #     # print("operations[i]", operations[i])
            #     record.append(int(operations[i]))

            if operations[i] == "C":
                record.pop()
                

            elif operations[i] == "D":
                len_of_record = len(record) - 1
                record.append(2 * record[len_of_record])


            elif operations[i] == "+":
                if len(record) > 0:
                    record.append(record[len(record) - 1] + (record[len(record) - 2]))

                else:
                    record.append(record[len_of_record] )

            else:
                try:
                    score = int(operations[i])
                    record.append(score)
                except ValueError:
                    print(f"Warning: Invalid operation '{operations[i]}' encountered.")


        print(sum(record))
        return sum(record)

object = Solution()
object.calPoints( ["5","-2","4","C","D","9","+","+"])
        