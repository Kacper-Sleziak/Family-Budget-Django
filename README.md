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

### Create Budget [POST]
Create budget and add to Budget List with id given in request. This operattio can be done by every user added to budget_list.
Category in body can be one of valid choices: Sport/Health/Insurance/Food/Travel
`Request /budget/create_budget/{budget_list_pk}`
`Body: money, title, description, category`




###
## How to use

