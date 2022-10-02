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

### Budget View Set [Get]
Return budgets for given params, accept only authenticated users.

`Request /budget`

`Params page, money_min, money_max, category, list, ordering`

page - number of the page, view is using pagination

money_min, money_max - can be used both or single, define range of money we want filter.

category - one of the choices Sport/Health/Insurance/Food/Travel

list - id of the budget_list, if we want get budget for specyfic budget_list we have to use this


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

