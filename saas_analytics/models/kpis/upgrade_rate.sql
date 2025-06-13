SELECT
  TIMESTAMP_TRUNC(timestamp, MONTH) AS month,
  COUNT(DISTINCT user_id) AS upgrades
from {{ source('saas_data', 'raw_events') }}
WHERE event_type = 'upgrade'
GROUP BY month
ORDER BY month DESC