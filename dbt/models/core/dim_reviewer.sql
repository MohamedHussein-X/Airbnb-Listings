{{
    config(
        materialized='table'
    )
}}


select 
    reviewer_id,
    reviewer_name
    from {{ref("stg_reviews_polarized")}}