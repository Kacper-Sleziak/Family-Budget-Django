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

### Create Budget List [POST]
Create budget list for authenticated user, one can have only one budget list

`Request /budget/lists/`

### Create Budget List [DELETE]
Delete Budget List, only creator of list can do this operation

`Request /budget/lists/{budget_list_pk}/`





###
## How to use

