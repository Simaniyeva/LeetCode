# Write your MySQL query statement below
SELECT E.Name as Employee from Employee E
LEFT JOIN Employee M
ON E.managerId=M.id
WHERE E.salary>M.salary