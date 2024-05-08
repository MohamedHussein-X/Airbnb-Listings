{{
    config(
        materialized = "table"
    )
}}

with 
    raw_date as ({{ dbt_date.get_date_dimension("2010-01-01", "2024-12-31") }})

select 
    row_number() over() as date_id,
    date_day,
    year_number,
    month_of_year,
    month_name_short,
    day_of_year,
    day_of_week_name,
    quarter_of_year
from raw_date 