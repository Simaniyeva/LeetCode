SELECT C1.name FROM
Customer C1
LEFT JOIN Customer C2
ON C1.id = C2.id
WHERE C1.referee_id != 2 OR C1.referee_id IS NULL