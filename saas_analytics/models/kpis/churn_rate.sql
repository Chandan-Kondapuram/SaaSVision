-- SELECT
--   TIMESTAMP_TRUNC(timestamp, MONTH) AS month,
--   COUNT(DISTINCT user_id) AS churned_users
-- FROM {{ source('saas_data', 'raw_events') }}
-- WHERE event_type = 'churn'
-- GROUP BY month
-- ORDER BY month DESC


SELECT
  TIMESTAMP_TRUNC(timestamp, MONTH) AS month,
  COUNT(DISTINCT CASE WHEN event_type = 'churn' THEN user_id END) AS churned_users,
  COUNT(DISTINCT user_id) AS total_users,
  SAFE_DIVIDE(
    COUNT(DISTINCT CASE WHEN event_type = 'churn' THEN user_id END),
    COUNT(DISTINCT user_id)
  ) AS churn_rate
FROM {{ source('saas_data', 'raw_events') }}
GROUP BY month
ORDER BY month DESC