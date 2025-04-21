
-- RFM-сегментация клиентов: финальный SQL
WITH base_rfm AS (
    SELECT
        customer_id,
        MAX(order_date) AS last_order_date,
        COUNT(*) AS frequency,
        SUM(amount) AS monetary
    FROM orders
    GROUP BY customer_id
),
rfm_with_recency AS (
    SELECT
        customer_id,
        DATE '2024-06-01' - last_order_date AS recency,
        frequency,
        monetary
    FROM base_rfm
),
scored_rfm AS (
    SELECT
        customer_id,
        recency,
        frequency,
        monetary,
        NTILE(5) OVER (ORDER BY recency DESC) AS r_score,
        NTILE(5) OVER (ORDER BY frequency) AS f_score,
        NTILE(5) OVER (ORDER BY monetary) AS m_score
    FROM rfm_with_recency
),
final_rfm AS (
    SELECT
        customer_id,
        recency, frequency, monetary,
        r_score, f_score, m_score,
        CONCAT(r_score, f_score, m_score) AS rfm_code,
        CASE
            WHEN r_score >= 4 AND f_score >= 4 AND m_score >= 4 THEN 'Champions'
            WHEN r_score <= 2 AND f_score >= 4 AND m_score >= 4 THEN 'At Risk Big Spender'
            WHEN r_score >= 4 AND f_score <= 2 THEN 'Potential Loyalist'
            WHEN r_score = 1 AND f_score = 1 AND m_score = 1 THEN 'Lost'
            ELSE 'Other'
        END AS segment
    FROM scored_rfm
)
SELECT * FROM final_rfm;