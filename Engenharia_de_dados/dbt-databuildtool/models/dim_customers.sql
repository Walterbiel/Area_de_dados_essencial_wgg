-- dbt model que limpa dados de clientes
SELECT
    customer_id,
    INITCAP(TRIM(customer_name)) AS customer_name,
    COALESCE(segment, 'unknown') AS segment
FROM {{ ref('stg_customers') }}
WHERE active = TRUE;
