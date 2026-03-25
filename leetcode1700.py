class Solution:
    def countStudents(self, students, sandwiches) -> int:

        # Keep looping as long as there are both students AND sandwiches left
        while students and sandwiches:
            front_student_pref = students[0]      # Get preference of student at front
            top_sandwich_type = sandwiches[0]     # Get type of sandwich on top

            if front_student_pref == top_sandwich_type:
                # Scenario 1: Match! Student takes the sandwich.
                # print(f"Student {front_student_pref} takes sandwich {top_sandwich_type}. Both leave.")
                students.pop(0)    # Remove student from front of queue
                sandwiches.pop(0)  # Remove sandwich from top of stack
                # print(f"  Remaining Students: {students}")
                # print(f"  Remaining Sandwiches: {sandwiches}\n")
            else:
                # Scenario 2: No match. Student doesn't like it.
                # print(f"Student {front_student_pref} does NOT like sandwich {top_sandwich_type}.")
                
                # Student goes to the end of the queue
                student_who_moved = students.pop(0) # Take student from front
                students.append(student_who_moved)  # Add student to the end
                # print(f"  Student {front_student_pref} moves to end. Students: {students}")
                # print(f"  Sandwiches remain: {sandwiches}\n") # Sandwich stack is unchanged

                # IMPORTANT: Check for the "stuck" condition here.
                # If the current top sandwich type is NOT found anywhere among the
                # remaining students in the queue, then no one will ever take it.
                # All remaining students are now unable to eat.
                if top_sandwich_type not in students:
                    print(f"Stuck! No remaining student wants sandwich {top_sandwich_type}. Stopping.")
                    break # Exit the while loop

        # The loop has finished. The number of students still in the 'students' list
        # are those who were unable to eat.
        return len(students)

object = Solution()
print(object.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))