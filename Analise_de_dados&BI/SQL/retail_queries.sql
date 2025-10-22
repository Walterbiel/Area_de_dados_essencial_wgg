-- Consulta de vendas totais por categoria
SELECT dp.category,
       ROUND(SUM(fs.quantity * fs.unit_price * (1 - fs.discount)), 2) AS revenue
FROM fact_sales fs
JOIN dim_product dp ON dp.product_id = fs.product_id
GROUP BY dp.category
ORDER BY revenue DESC;

-- Consulta de ticket médio por segmento de cliente
SELECT dc.segment,
       ROUND(SUM(fs.quantity * fs.unit_price * (1 - fs.discount)) / SUM(fs.quantity), 2) AS average_ticket
FROM fact_sales fs
JOIN dim_customer dc ON dc.customer_id = fs.customer_id
GROUP BY dc.segment;
