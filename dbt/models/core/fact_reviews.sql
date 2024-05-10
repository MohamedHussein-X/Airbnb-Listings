{{
    config(
        materialized='table'
    )
}}


with dim_date as (
     select * from {{ref("dim_date")}}
), 

dim_comments as (
    select * from {{ref('dim_comments')}}
),

dim_reviewer as (
    select * from {{ref('dim_reviewer')}}
), 
stg_reviews_polarized as (
    select * from {{ref('stg_reviews_polarized')}}
)


select 
    review_id ,
    pos_score,
    neg_score,
    neu_score,
    listing_id,
    dim_date.date_id as date_id ,
    reviewer_id as reviewer_id
    from stg_reviews_polarized
    inner join   dim_date on
    dim_date.date_day = stg_reviews_polarized.date
