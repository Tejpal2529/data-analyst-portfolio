
-- EMPLOYEE SQL ANALYSIS PROJECT

-- 1. Display all employees
SELECT * FROM employees;

-- 2. Find IT employees
SELECT *
FROM employees
WHERE department = 'IT';

-- 3. Find employees earning above £30,000
SELECT *
FROM employees
WHERE salary > 30000;

-- 4. Sort employees by salary
SELECT *
FROM employees
ORDER BY salary DESC;

-- 5. Count employees by department
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;

-- 6. Calculate average salary
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

-- 7. Combine employee and department tables
SELECT employees.name,
       employees.department,
       departments.location
FROM employees
INNER JOIN departments
ON employees.department = departments.department_name;

-- 8. Calculate total salary by department
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

-- 9. Filter departments by average salary
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 30000;

-- 10. Categorise employees by salary
SELECT name, department, salary,
CASE
    WHEN salary >= 40000 THEN 'High Salary'
    WHEN salary >= 30000 THEN 'Medium Salary'
    ELSE 'Low Salary'
END AS salary_category
FROM employees;
