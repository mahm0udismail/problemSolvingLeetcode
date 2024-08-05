# Write your MySQL query statement below
select p.project_id  , ROUND(AVG(e.experience_years),2) AS average_years 
from Employee e join Project p
on e.employee_id = p.employee_id
group by project_id