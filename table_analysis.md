## Table sizes:

### < 200 rows:

- adminuser (19 rows)
- alembic_version (1 row)
- campaign (8 rows)
- discount (60 rows)
- invoice (0 rows)
- ncustomer (149 rows)
- packing_order_queue_entry (3 rows)
- payment_gateway (9 rows)
- payment_summary (0 rows)
- paymentmethods (155 rows)
- printer (2 rows)
- product_categories (61 rows)
- product_type_info (57 rows)
- seller (2 rows)
- seller_payment_gateway_association (10 rows)
- shipping_service (15 rows)
- supplier (5 rows)

### 200 - 10000 rows:

- customer_log (1237 rows)
- customerdetails (757 rows)
- order (1677 rows)
- order_discount (509 rows)
- order_source (1599 rows)
- orderitem (3876 rows)
- paymentdetails (3190 rows)
- product (3234 rows)
- product_group_info (477 rows)
- purchase (1257 rows)

### 10000+ rows:

- comments (16141 rows)
- in_pincode (26829 rows)
- order_log (11092 rows)
- product_log (8889504 rows)
- uk_pincode (1755571 rows)

## Tables that may contain sensitve data

- adminuser (not customer-related)
  - first_name
  - email
  - password
- comments
  - comment_text?
- customer_log
  - email
  - token?
- customerdetails
  - full_name
  - phone
  - address1
  - address2
- ncustomer
  - email
  - token?
- paymentdetails
  - billing_ref
  - bank_ref
- seller (not customer-related)
  - address1
  - address2
  - tax_id_number
  - email
- supplier (not customer-related)
  - address1
  - address2
  - email
  - phone
