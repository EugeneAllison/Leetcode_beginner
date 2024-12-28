from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q1, q2 = deque(), deque()
        for student in students:
            q1.append(student)
        for sandwich in sandwiches:
            q2.append(sandwich)

        for _ in range(50 * len(students)):
            if not students:
                break  # Exit the loop if students list is empty
            if q2 and q2[0] == q1[0]:
                q2.popleft()
                q1.popleft()
            elif q2 and q2[0] != q1[0]:
                q1.append(q1.popleft())
            else:
                continue

        return len(q1)
