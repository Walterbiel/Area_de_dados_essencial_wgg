-- Consolidação de clientes com dados de churn
CREATE TABLE IF NOT EXISTS stg_customers (
    customer_id INTEGER PRIMARY KEY,
    status TEXT NOT NULL,
    signup_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS stg_usage (
    customer_id INTEGER NOT NULL,
    month TEXT NOT NULL,
    consumption INTEGER NOT NULL
);

CREATE VIEW IF NOT EXISTS vw_churn_features AS
SELECT
    c.customer_id,
    c.status,
    COUNT(u.month) AS active_months,
    AVG(u.consumption) AS avg_consumption
FROM stg_customers c
LEFT JOIN stg_usage u ON u.customer_id = c.customer_id
GROUP BY c.customer_id, c.status;
