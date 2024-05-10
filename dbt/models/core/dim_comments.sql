
{{
    config(
        materialized='table'
    )
}}

select 
    review_id, 
    comments
    from {{ref("stg_reviews_polarized")}}
