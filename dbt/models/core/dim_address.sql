{{
    config(
        materialized='table'
    )
}}

select 
        {{ dbt_utils.generate_surrogate_key(['longitude','latitude']) }} as address_id,
        zipcode,
        street,
        neighbourhood_cleansed,
        latitude,
        longitude,
    from      {{ ref('stg_airbnb_listings') }}
