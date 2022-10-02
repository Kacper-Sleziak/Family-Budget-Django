# Family Budget

## Description
Family Budget is the backend of an application created to help people manage their money with few useful tools.

## Technology Stack
Backend created with help od **Django** with **REST framework**.

**PostgreSQL** as a data base.

**Docker** for deplyoing local environment.

## Concept 
1. One user can have one budget list
2. On the other hand user can be a participant of many budget lists
3. Every budget list have budgets and a list of users who can manage them
4. Every budget consists of transactions which can be income or expenses

## API Documentation

### Permissions
Requests that need authentication should contain header with
`"Authorization" : "Token {Token_key}"`


### Login [POST]
Returns login credentials and informations about user

`Request /user/login`

`Body: email, password`

### Register [POST]

`Request /user/register`

`Body: email, password, password2, first_name, last_name`

### Budget View Set [GET]
Returns budgets for given params, accept only authenticated users.

`Request /budget`

`Params page, money_min, money_max, category, list, ordering`

*page* - number of the page, view is using pagination.

*page_size* - change standard size of pagination.

*money_min*, money_max - can be used both or single, define range of money we want filter.

*category* - one of the choices Sport/Health/Insurance/Food/Travel.

*list* - id of the budget_list, if we want get budgets for specyfic budget_list we have to use this.

### Budget List View Set [GET]
Returns budget lists
`Request /budget/lists`

### Budget List Add User [PATCH]
Adds user to budget list. Operation can be done only by creator of the list.

`Request /budget/lists/{list_pk}add_new_user/`

`Body: user` 

*user in body stands for user's pk*

### Create Transcation [POST]
Creates transaction for given in request pk of budget. 

`Request /budget/create_transaction/{budget_pk}`

`Body: delta_money, title`

For expense delta_money should have ,,-" before number

### Create Budget List [POST]
Creates budget list for authenticated user, one can have only one budget list

`Request /budget/lists/`

### Create Budget List [DELETE]
Delete Budget List, only creator of list can do this operation

`Request /budget/lists/{budget_list_pk}/`

### Create Budget [POST]
Create a budget and add it to Budget List with the id given in the request. This operation can be done by every user added to budget_list.
Category in the body can be one of the valid choices: Sport/Health/Insurance/Food/Travel

`Request /budget/create_budget/{budget_list_pk}`

`Body: money, title, description, category`

## Deploying in local environment
1. Clone Repository
2. Create `.env` file in backend folder
3. Paste to .env: 

`SECRET_KEY=`

`DEBUG=`

`POSTGRES_DB=`

`POSTGRES_USER=`

`POSTGRES_PASSWORD=`

`POSTGRES_PORT=`

Sample how should `.env` look you can find in `.env_template`. 

To generate custome django key i strongely recommend to use this website <a>https://djecrety.ir</a>

4. Install Docker
5. In `/backend` open terminal and run these commands:

`docker-compose build` - to pull and build images

`docker-compose up -d` - to run project, `-d` flag is optional

6. Finally you can find django working on <a>http://localhost:8000/</a>



