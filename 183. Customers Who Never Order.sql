SELECT C.name as 'Customers' from Customers C
LEFT JOIN  Orders O
ON C.id=O.customerId
WHERE O.customerId IS NULL