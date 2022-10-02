# Family Budget

## Description 

## Concept 

## Data Base Diagram

## API

### Login [POST]
Return login credentials and informations about user

`Request /user/login`

`Body: email, password`

### Register [POST]

`Request /user/register`

`Body: email, password, password2, first_name, last_name`

### Create Transcation [POST]
Create transaction for given in request pk of budget

`Request /budget/create_transaction/{budget_pk}`

`Body: delta_money, title`


###
## How to use

