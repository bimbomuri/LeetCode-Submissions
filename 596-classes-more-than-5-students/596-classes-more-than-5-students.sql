/* Write your T-SQL query statement below */


select a.class as class from (
select class,count(distinct student) 
    as num from Courses group by class )a where a.num >=5