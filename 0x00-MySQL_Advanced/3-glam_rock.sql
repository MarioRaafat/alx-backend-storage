-- two columns ordered by 
SELECT 
    band_name, 
    (IFNULL(split, 2020) - formed) AS lifespan
FROM
    metal_bands
WHERE 
    IFNULL(style, " ") LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;