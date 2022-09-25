/* Write your T-SQL query statement below */

select c.name as Customers from (
select a.id,a.name,b.customerId,b.Id as table_id from Customers as a left join Orders as b on (a.id = b.customerId))  c
where c.table_id is NULL