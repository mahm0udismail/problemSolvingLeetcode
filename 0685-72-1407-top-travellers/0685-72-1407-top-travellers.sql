# Write your MySQL query statement below
select name , sum(if(distance is NULL,0,distance)) as travelled_distance
from Users left join Rides 
on Users.id = Rides.user_id
group by Users.id
order by travelled_distance desc, name asc