# Leetcode SQL problems

# Combine two tables - easy

# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName, Address.City, Address.State
FROM Person left join Address ON Person.PersonId = Address.PersonId



# Duplicate Emails - easy

SELECT Email 
FROM (SELECT DISTINCT(Email), COUNT(Email) as Num
     FROM Person) as stats
WHERE stats.Num > 1     


# Bug countries - easy
SELECT name, population, area
FROM World
WHERE population > 25000000 or area > 3000000


# Classes more than five students - easy
select class 
from (select class, COUNT(class) as num 
      from courses) as stats
where stats.num >= 5    


# Not Boring Movies
select id, movie, description, rating
from cinema
where description != "boring" and id % 2 = 1
order by rating desc

Result:
Success
Details
Runtime: 505 ms, faster than 5.10% of MySQL online submissions for Not Boring Movies.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Not Boring Movies.




