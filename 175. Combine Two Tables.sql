/* Write your T-SQL query statement below */
SELECT P.firstName, P.lastName, A.city, A.state from Person P
LEFT JOIN Address A
ON A.personId=P.personID