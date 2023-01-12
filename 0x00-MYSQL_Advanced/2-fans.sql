-- query to get the number of fans for bands based on their origin
SELECT origin, SUM(fans) as nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;