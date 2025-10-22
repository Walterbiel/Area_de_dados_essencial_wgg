-- Sales star schema for BI analysis
CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY,
    date_value TEXT NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    segment TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id INTEGER PRIMARY KEY,
    date_id INTEGER NOT NULL REFERENCES dim_date(date_id),
    customer_id INTEGER NOT NULL REFERENCES dim_customer(customer_id),
    product_id INTEGER NOT NULL REFERENCES dim_product(product_id),
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    discount REAL DEFAULT 0.0,
    CONSTRAINT chk_quantity_positive CHECK (quantity > 0),
    CONSTRAINT chk_unit_price_positive CHECK (unit_price >= 0),
    CONSTRAINT chk_discount_range CHECK (discount BETWEEN 0 AND 1)
);

-- View to expose total revenue by product category
CREATE VIEW IF NOT EXISTS vw_revenue_by_category AS
SELECT
    dp.category,
    SUM(fs.quantity * fs.unit_price * (1 - fs.discount)) AS revenue
FROM fact_sales fs
JOIN dim_product dp ON dp.product_id = fs.product_id
GROUP BY dp.category;
