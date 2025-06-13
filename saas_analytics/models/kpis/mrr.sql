SELECT
  TIMESTAMP_TRUNC(timestamp, MONTH) AS month,
  SUM(amount) AS mrr
from {{ source('saas_data', 'raw_events') }}
WHERE event_type = 'subscription_renewal'
GROUP BY month
ORDER BY month DESC