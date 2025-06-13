SELECT
  user_id,
  COUNT(*) AS login_events,
  COUNT(*) / COUNT(DISTINCT DATE(timestamp)) AS avg_logins_per_day
FROM {{ source('saas_data', 'raw_events') }}
WHERE event_type = 'login'
GROUP BY user_id