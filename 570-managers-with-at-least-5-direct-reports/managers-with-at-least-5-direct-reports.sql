# Write your MySQL query statement below
SELECT e2.name
FROM Employee  e1
LEFT JOIN Employee e2
ON e1.managerID = e2.id
WHERE e2.id is not NULL 
GROUP BY e2.id
HAVING COUNT(e2.id) >= 5