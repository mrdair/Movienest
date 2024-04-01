WITH popularity_agg AS (
    SELECT 
    TO_CHAR(TO_DATE(release_date, 'YYYY-MM-DD'), 'MMMM') AS month_name,
    ROUND(AVG(popularity), 2) AS popularity
FROM 
    {{ ref("tmdb_movies_models") }}
WHERE 
    release_date != ''
GROUP BY 
    month_name
)


SELECT
    month_name AS release_month,
    popularity
FROM popularity_agg Order by MONTH(TO_DATE(month_name, 'Mon'))

