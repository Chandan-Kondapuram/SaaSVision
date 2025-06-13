SELECT
  DATE(timestamp) AS date,
  COUNT(DISTINCT user_id) AS daily_active_users
from {{ source('saas_data', 'raw_events') }}
WHERE event_type = 'login'
GROUP BY date
ORDER BY date DESC