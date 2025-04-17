# Write your MySQL query statement below
select product_name , sum(Orders.unit) AS unit
from Products join Orders
on Products.product_id = Orders.product_id
where date_format(Orders.order_date,'%Y-%m')='2020-02'
group by Orders.product_id 
having unit>=100