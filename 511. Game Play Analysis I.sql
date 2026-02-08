# Write your MySQL query statement below
SELECT A.player_id,Min(A.event_date) first_login
FROM Activity A
GROUP BY A.player_id