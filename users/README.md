# **Users**

Used to manage user account.  
GET and PUT endpoints are always in context of current logged-in user, taken from Bearer token.

## 1. Get user details

**Description:** Gets current user details.

**URL:** `/users/`

**Method:** `GET`

**Auth required:** Yes

### Success Response

**Code:** `200 OK`

**Content example:**

```json
{
    "id": 1,
    "email": "email@em.em",
    "gender": "M",
    "birth_date": "2020-12-02",
    "monthly_limit": 100.0,
    "income_range": 5,
    "date_joined": "2020-12-19T17:35:30.328392Z",
    "allow_data_collection": true
}
```

### Error Responses

**Condition:** If access token expired.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Access token expired"
}
```
&nbsp;

## 2. Create new user

**Description:** Creates new user.

**URL:** `/users/`

**Method:** `POST`

**Auth required:** No

**Body fields:**
* **email** - user email  
  *Required:* true  
  *Format:* Email format  
  *Unique:* true
* **password** - user password  
  *Required:* true  
  *Min length:* 5  
  *Max length:* 250  
  *Format:* min. 1 number and 1 special character
* **gender** - user gender  
  *Required:* true  
  *Max length:* 1  
  *Format:* 'F' or 'M'
* **birth_date** - user birthday date  
  *Required:* true  
  *Format:* yyyy-MM-dd  
* **monthly_limit** - user monthly expenses value limit  
  *Required:* false  
* **income_range** - id of the [income range](https://github.com/PKapski/Expensis-server/tree/development/commons#1-income-ranges)  
  *Required:* true  
* **username** - user's username  
  *Required:* true  
  *Max length:* 150  
  *Unique:* true
* **allow_data_collection** - determines if user allows application to collect his data to create statistics.
  If set to false, user won't be allowed to use statistics functionality.  
  *Required:* false  
  *Default:* false  
  
**Example body:**
```json
{
    "email": "email@em.em",
    "password": "pass1!",
    "gender": "M",
    "birth_date": "2000-12-02",
    "monthly_limit": 100.0,
    "income_range": 1,
    "username": "username",
    "allow_data_collection": true
}
```
### Success Response

**Code:** `201 Created`

**Content example:**

```json
{
    "id": 1,
    "email": "email@em.em",
    "password": "pass1!",
    "gender": "M",
    "birth_date": "2000-12-02",
    "monthly_limit": 100.0,
    "income_range": 1,
    "allow_data_collection": true
}
```

### Error Responses

**Condition:** Empty required field, wrong date format, invalid income range id

**Code:** `400 Bad request`

**Content:**

```json
{
  "date": [
    "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
  ],
  "title": [
    "This field is required."
  ]
}
```
***

**Condition:** If access token expired.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Access token expired"
}
```
&nbsp;

## 3. Edit user data

**Description:** Edits user data.

**URL:** `/users/`

**Method:** `PUT`

**Auth required:** Yes

**Body fields:**
* **email** - user email  
  *Required:* true  
  *Format:* Email format  
  *Unique:* true
* **password** - user password  
  *Required:* true  
  *Min length:* 5  
  *Max length:* 250  
  *Format:* min. 1 number and 1 special character
* **gender** - user gender  
  *Required:* true  
  *Max length:* 1  
  *Format:* 'F' or 'M'
* **birth_date** - user birthday date  
  *Required:* true  
  *Format:* yyyy-MM-dd  
* **monthly_limit** - user monthly expenses value limit  
  *Required:* false  
* **income_range** - id of the [income range](https://github.com/PKapski/Expensis-server/tree/development/commons#1-income-ranges)  
  *Required:* true
* **allow_data_collection** - determines if user allows application to collect his data to create statistics.
  If set to false, user won't be allowed to use statistics functionality.  
  *Required:* false  
  *Default:* false  
  
**Example body:**
```json
{
    "email": "email@em.em",
    "password": "pass1!",
    "gender": "M",
    "birth_date": "2000-12-02",
    "monthly_limit": 100.0,
    "income_range": 1,
    "allow_data_collection": true
}
```
### Success Response

**Code:** `200 OK`

**Content example:**

```json
{
    "id": 1,
    "email": "email@em.em",
    "password": "pass1!",
    "gender": "M",
    "birth_date": "2000-12-02",
    "monthly_limit": 100.0,
    "income_range": 1,
    "allow_data_collection": true
}
```

### Error Responses

**Condition:** Empty required field, wrong date format, invalid income range id

**Code:** `400 Bad request`

**Content:**

```json
{
  "date": [
    "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
  ],
  "title": [
    "This field is required."
  ]
}
```
***

**Condition:** If access token expired.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Access token expired"
}
```