
SELECT mcc
FROM receipts
WHERE EXTRACT(YEAR FROM datetime) = 2023 AND EXTRACT(MONTH FROM datetime) = 11
GROUP BY mcc
ORDER BY COUNT(*) DESC
LIMIT 1;


WITH ranked_mccs AS (
    SELECT mcc, COUNT(*) AS frequency, RANK() OVER (ORDER BY COUNT(*) DESC) AS rank
    FROM receipts
    WHERE EXTRACT(YEAR FROM datetime) = 2023 AND EXTRACT(MONTH FROM datetime) = 11
    GROUP BY mcc
)
SELECT mcc
FROM ranked_mccs
WHERE rank = 1;
