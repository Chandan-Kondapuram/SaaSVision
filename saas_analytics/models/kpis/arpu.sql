SELECT
  TIMESTAMP_TRUNC(timestamp, MONTH) AS month,
  ROUND(SUM(amount) / COUNT(DISTINCT user_id), 2) AS arpu
from {{ source('saas_data', 'raw_events') }}
WHERE event_type IN ('payment', 'subscription_renewal')
GROUP BY month
ORDER BY month DESC