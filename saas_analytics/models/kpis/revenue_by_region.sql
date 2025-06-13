SELECT
  region,
  SUM(amount) AS revenue
from {{ source('saas_data', 'raw_events') }}
WHERE event_type IN ('payment', 'subscription_renewal')
GROUP BY region
ORDER BY revenue DESC