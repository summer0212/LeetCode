class Solution:
    def minMovesToSeat(self, seats, students) :
        move = 0

        sorted_seats = sorted(seats)
        sorted_student = sorted(students)

        j = 0
        for i in range(len(sorted_seats)):
            move += abs(sorted_seats[i] - sorted_student[j])
            j += 1

        return move

''' Alternate logic:
def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)
        output = 0

        for i in range(0,len(sorted_students)):
            output += abs(sorted_students[i] - sorted_seats[i])

        return output'''


object = Solution()
print(object.minMovesToSeat([3,1,5], [2,7,4]))

