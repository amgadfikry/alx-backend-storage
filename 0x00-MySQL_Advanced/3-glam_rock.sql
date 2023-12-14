-- script that lists all bands with Glam rock as their main style, ranked by their longevity
-- select the specific column with requirements
SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
  FROM metal_bands
  WHERE style LIKE '%Glam rock%'
  ORDER by lifespan DESC;
