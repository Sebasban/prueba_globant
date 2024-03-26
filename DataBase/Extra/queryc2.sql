WITH tbl AS (
            SELECT
                id,
                department_id,
                job_id,
                CONVERT(
                    CONCAT(
                        SUBSTRING(datetime, 1, 4),
                        SUBSTRING(datetime, 6, 2)
                    ),
                    UNSIGNED INTEGER
                ) AS ano_mes
            FROM
                DBTG.hired_employees
        ),
        trimestre AS (
            SELECT
                id,
                department_id,
                job_id,
                ano_mes,
                CASE 
                    WHEN ano_mes >= 202101 AND ano_mes <= 202103 THEN 'Q1'
                    WHEN ano_mes >= 202104 AND ano_mes <= 202106 THEN 'Q2'
                    WHEN ano_mes >= 202107 AND ano_mes <= 202109 THEN 'Q3'
                    WHEN ano_mes >= 202110 AND ano_mes <= 202112 THEN 'Q4'
                END AS trimestre
            FROM
                tbl
            WHERE
                ano_mes < 202201
        ),
        departments AS (
            SELECT
                t1.id,
                t1.department_id,
                t1.job_id,
                t1.ano_mes,
                t1.trimestre,
                t2.department
            FROM
                trimestre t1
            LEFT JOIN
                DBTG.departments t2 ON t1.department_id = t2.id
        ),
        jobs AS (
            SELECT 
                t1.id,
                t1.department_id,
                t1.job_id,
                t1.ano_mes,
                t1.trimestre,
                t1.department,
                t2.job
            FROM 
                departments t1 
            LEFT JOIN 
                DBTG.jobs t2 ON t1.job_id = t2.id
        )
        SELECT
            department,
            job,
            SUM(CASE WHEN trimestre = 'Q1' THEN 1 ELSE 0 END) AS Q1,
            SUM(CASE WHEN trimestre = 'Q2' THEN 1 ELSE 0 END) AS Q2,
            SUM(CASE WHEN trimestre = 'Q3' THEN 1 ELSE 0 END) AS Q3,
            SUM(CASE WHEN trimestre = 'Q4' THEN 1 ELSE 0 END) AS Q4
        FROM
            jobs 
        GROUP BY
            department, job
        ORDER BY 1, 2



WITH count as (
    SELECT
        COUNT(*) AS cnt
    FROM
        hired_employees
    WHERE
        SUBSTRING(datetime, 1, 4) = '2021'
    GROUP BY
        department_id
),
MeanHires AS (
    SELECT
        AVG(cnt) AS mean_hires
    FROM
        count
),
DepartmentHireCounts AS (
    SELECT
        department_id,
        COUNT(*) AS num_hires
    FROM
        hired_employees
    GROUP BY
        department_id
),
DepartmentHires AS (
    SELECT
        t2.id AS department_id,
        t2.department,
        t1.num_hires
    FROM
        DepartmentHireCounts t1
        INNER JOIN departments t2 ON t1.department_id = t2.id
)
SELECT
    t1.department_id AS id,
    t1.department,
    t1.num_hires AS hired
FROM
    DepartmentHires t1
    INNER JOIN MeanHires t2 ON t1.num_hires > t2.mean_hires
ORDER BY
    t1.num_hires DESC;