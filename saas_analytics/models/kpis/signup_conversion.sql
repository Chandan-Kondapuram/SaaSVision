SELECT
  COUNT(DISTINCT user_id) AS trial_signups,
  COUNT(DISTINCT CASE WHEN is_trial = FALSE THEN user_id END) AS converted_to_paid,
  ROUND(
    COUNT(DISTINCT CASE WHEN is_trial = FALSE THEN user_id END) * 100.0 /
    NULLIF(COUNT(DISTINCT user_id), 0), 2
  ) AS conversion_rate_percent
from {{ source('saas_data', 'raw_events') }}
WHERE event_type = 'signup'