SELECT
  region,
  COUNT(DISTINCT user_id) AS active_users
from {{ source('saas_data', 'raw_events') }}
WHERE event_type = 'login'
GROUP BY region
ORDER BY active_users DESC