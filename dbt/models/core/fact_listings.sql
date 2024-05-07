{{
    config(
        materialized='table'
    )
}}

with dim_address as (
    select * from {{ref("dim_address")}}
),

dim_date as (
    select * from {{ref("dim_date")}}
),

listings as ( 
    select * from {{ ref('stg_airbnb_listings')}}
),

dim_listings_info as (
    select * from {{ref ('dim_listing_info')}}
),

dim_host as (
    select * from {{ref('dim_host')}}
)

select 
    listings.listing_id,
    listings.price,
    listings.host_id,
    dim_address.address_id,
    dim_date.date_id    
from listings 
    inner join dim_date on listings.host_since = dim_date.date_day
    inner join dim_address on listings.latitude = dim_address.latitude 
                            and listings.longitude = dim_address.longitude
    inner join dim_listings_info 
    on listings.listing_id = dim_listings_info.listing_id
    inner join dim_host 
    on listings.host_id = dim_host.host_id
    