
SELECT card_number
FROM cards
ORDER BY balance ASC
LIMIT 10;


WITH ranked_cards AS (
    SELECT card_number, ROW_NUMBER() OVER (ORDER BY balance ASC) AS rank
    FROM cards
)
SELECT card_number
FROM ranked_cards
WHERE rank <= 10;
