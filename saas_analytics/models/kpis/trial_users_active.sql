SELECT
  user_id,
  MAX(timestamp) AS last_seen
from {{ source('saas_data', 'raw_events') }}
WHERE is_trial = TRUE AND event_type = 'login'
GROUP BY user_id