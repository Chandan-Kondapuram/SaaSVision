SELECT
  user_id,
  SUM(amount) AS lifetime_value
from {{ source('saas_data', 'raw_events') }}
WHERE event_type IN ('payment', 'subscription_renewal')
GROUP BY user_id
ORDER BY lifetime_value DESC