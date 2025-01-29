SELECT
    r.report_id,
    COUNT(p.product_id) AS number_of_products,
    SUM(p.price) AS total_sum,
    MAX(p.price) AS max_product_price
FROM reports r
JOIN transactions_products_dict tpd ON r.tran_id = tpd.tran_id
JOIN products p ON tpd.product_id = p.product_id
GROUP BY r.report_id;
