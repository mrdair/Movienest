WITH genres_agg AS (
    SELECT
        CASE
            WHEN GENRES LIKE '%Action%' THEN 'Action'
            WHEN GENRES LIKE '%Comedy%' THEN 'Comedy'
            WHEN GENRES LIKE '%Drama%' THEN 'Drama'
            WHEN GENRES LIKE '%Documentary%' THEN 'Documentary'
            WHEN GENRES LIKE '%Animation%' THEN 'Animation'
            WHEN GENRES LIKE '%Music%' THEN 'Music'
            WHEN GENRES LIKE '%Romance%' THEN 'Romance'
            WHEN GENRES LIKE '%Horror%' THEN 'Horror'
            WHEN GENRES LIKE '%Thriller%' THEN 'Thriller'
            WHEN GENRES LIKE '%Western%' THEN 'Western'
            ELSE 'Other'
        END AS genre_category,
        COUNT(*) AS movie_count
    FROM {{ ref('tmdb_movies_models') }}
    WHERE STATUS = 'Released' 
    GROUP BY genre_category
)

SELECT
    genre_category,
    movie_count
FROM genres_agg
Order by 2 desc