with 

source as (

    select * from {{ source('staging', 'airbnb_listings') }}

),

renamed as (

    select
        safe_cast(id as INTEGER) as listing_id,
        safe_cast(host_id as INTEGER) as host_id,
        cast(host_name as STRING) as host_name,
        cast(host_since as DATE) as host_since,
        cast(host_response_time as STRING) as host_response_time,
        cast(name as STRING) as name,
        cast(summary as STRING) as summary,
        cast(space as STRING) as space,
        cast(description as STRING) as description,
        cast(amenities as STRING) as amenities,
        cast(property_type as STRING) as property_type,
        cast(room_type as STRING) as room_type,
        safe_cast(accommodates as INTEGER) as num_accommodates,
        safe_cast(bathrooms as FLOAT64) as num_bathrooms,
        safe_cast(bedrooms as FLOAT64) as num_bedrooms,
        safe_cast(beds as FLOAT64) as num_beds,
        cast(instant_bookable as STRING) as instant_bookable,
        cast(cancellation_policy as STRING ) as cancellation_policy,
        cast(neighborhood_overview as STRING) as neighborhood_overview,
        cast(neighbourhood_cleansed as STRING) as neighbourhood_cleansed,
        safe_cast(longitude as FLOAT64) as longitude,
        safe_cast(latitude as FLOAT64) as latitude,
        cast(street as STRING) as street,
        safe_cast(zipcode as INTEGER) as zipcode,
        safe_cast(review_scores_rating as FLOAT64) as review_scores_rating,
        safe_cast(reviews_per_month as FLOAT64) as reviews_per_month,
        safe_cast(number_of_reviews as INTEGER) as number_of_reviews,
        safe_cast(price as FLOAT64) as price
    from source

)

select * from renamed
