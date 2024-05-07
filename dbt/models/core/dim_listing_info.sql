{{
    config(
        materialized='table'
    )
}}


select 
    listing_id, 
    property_type, 
    room_type,
    num_accommodates,
    num_bathrooms,
    num_bedrooms,
    num_beds,
    CAST(SPLIT(REGEXP_REPLACE(REGEXP_REPLACE(amenities, '{', ''), '}', ''), ',') AS ARRAY<STRING>) as amenities,
    instant_bookable,
    cancellation_policy
from {{ref("stg_airbnb_listings")}}