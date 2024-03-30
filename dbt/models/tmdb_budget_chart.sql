WITH budget_agg AS (
    SELECT
        ROUND(SUM(budget)) AS total_budget,
        DATE_PART('YEAR', TO_DATE(release_date, 'YYYY-MM-DD')) AS release_year
    FROM {{ ref("tmdb_movies_models") }} t
    WHERE release_date != ''
        AND DATE_PART('YEAR', TO_DATE(release_date, 'YYYY-MM-DD')) BETWEEN 1990 AND 2023
    GROUP BY DATE_PART('YEAR', TO_DATE(release_date, 'YYYY-MM-DD'))
)

SELECT
    total_budget AS "Total budget",
    release_year AS "RELEASE YEAR"
FROM budget_agg
ORDER BY release_year
