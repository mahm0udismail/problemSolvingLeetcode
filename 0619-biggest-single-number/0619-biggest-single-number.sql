select MAX(num) AS num
from (
    select num 
    from MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)AS unique_numbers;
