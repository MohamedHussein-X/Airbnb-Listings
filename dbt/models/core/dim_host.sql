{{
    config(
        materialized='table'
    )
}}

select 
    host_id,
    host_name,
    host_since,
    host_response_time,
    from {{ref("stg_airbnb_listings")}}
    