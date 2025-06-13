SELECT
  TIMESTAMP_TRUNC(timestamp, MONTH) AS month,
  SUM(amount) AS payment_volume
from {{ source('saas_data', 'raw_events') }}
WHERE event_type = 'payment'
GROUP BY month
ORDER BY month DESC