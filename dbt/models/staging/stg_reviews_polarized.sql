with 

source as (

    select * from {{ source('staging', 'reviews_polarized') }}

),

renamed as (

    select
        {{ dbt.safe_cast("id", api.Column.translate_type("integer")) }} as review_id,
        {{ dbt.safe_cast("listing_id", api.Column.translate_type("integer")) }} as listing_id,
        cast(date as DATE) as date_time,
        {{ dbt.safe_cast("reviewer_id", api.Column.translate_type("integer")) }} as reviewer_id,
        cast(reviewer_name as STRING  ) as reviewer_name,
        cast(comments as STRING ) as comments ,
        cast (pos as numeric ) as pos_score,
        cast ( neg as numeric) as neg_score,
        cast (neu as numeric ) as neu_score,
        cast(compound as numeric ) as compound_score

    from source

)

select * from renamed
