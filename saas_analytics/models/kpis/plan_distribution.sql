SELECT
  plan,
  COUNT(DISTINCT user_id) AS user_count
from {{ source('saas_data', 'raw_events') }}
WHERE event_type = 'signup'
GROUP BY plan
ORDER BY user_count DESC