-- Write your query below
select name from customers c 
left join orders o on o.customer_id = c.id
where o.customer_id is null