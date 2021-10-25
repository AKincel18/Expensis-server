# **Expenses**

Used to manage user expenses and fetch certain month sum.  
Every endpoint listed here is in context of user, which is taken from Bearer token.

## 1. Get expenses list

**Description:** Returns expenses list

**URL:** `/expenses/`

**Method:** `GET`

**Auth required:** Yes

**Query params:** 
* **title** - filters expenses that contain given string
* **year** - filters expenses from given year. Defaults by current year
* **month** - filters expenses from given month. Defaults by current month
* **pageSize** - used for pagination. Size of single page
* **pageIndex** - used for pagination. Page index

**Return headers:**
* **X-MAX-RESULTS** - returns number of expenses without pagination
### Success Response

**Code:** `200 OK`

**Content example:**

```json
[
    {
        "id": 1,
        "user": 1,
        "date": "2021-01-26",
        "title": "title",
        "description": "description",
        "category": "category",
        "value": "100.00"
    },
    {
        "id": 2,
        "user": 1,
        "date": "2021-01-26",
        "title": "title",
        "description": "description",
        "category": "category",
        "value": "100.00"
    }
]
```

### Error Response

**Condition:** If access token expired.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Access token expired"
}
```
&nbsp;

## 2. Add expense

**Description:** Adds new expense.

**URL:** `/expenses/`

**Method:** `POST`

**Auth required:** Yes

**Body fields:**
* **date** - expense date  
  *Required:* false  
  *Format:* yyyy-MM-dd  
  *Default:* today
* **title** - expense title  
  *Required:* true  
  *Max length:* 80
* **description** - expense description  
  *Required:* false  
  *Max length:* 150
* **category** - id of the expense [category](https://github.com/AKincel18/Expensis-server/tree/development/commons#3-categories)  
  *Required:* true  
* **value** - expense value  
  *Required:* true  
  *Decimal places:* 2  
  *Max digits:* 19
  
**Example body:**
```json
{
    "date": "2021-02-10",
    "title": "title",
    "description": "description",
    "category": 1,
    "value": 1000
}
```
### Success Response

**Code:** `201 Created`

**Content example:**

```json
{
    "id": 1,
    "user": 1,
    "date": "2021-02-10",
    "title": "title",
    "description": "description",
    "category": "Food",
    "value": "1000.00"
}
```

### Error Responses

**Condition:** Negative value, empty required field, wrong date format, invalid category id

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

## 3. Get expense details

**Description:** Gets single expense details.

**URL:** `/expenses/{expense_id}/`

**Method:** `GET`

**Auth required:** Yes

### Success Response

**Code:** `200 OK`

**Content example:**

```json
{
    "id": 1,
    "user": 1,
    "date": "2021-02-10",
    "title": "title",
    "description": "description",
    "category": "Food",
    "value": "1000.00"
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
***
**Condition:** Invalid expense id

**Code:** `404 Not found`

**Content:** `{}`

## 4. Edit expense

**Description:** Edits expense.

**URL:** `/expenses/{expense_id}/`

**Method:** `PUT`

**Auth required:** Yes

**Body fields:**
* **date** - expense date  
  *Required:* false  
  *Format:* yyyy-MM-dd  
  *Default:* today
* **title** - expense title  
  *Required:* true  
  *Max length:* 80
* **description** - expense description  
  *Required:* false  
  *Max length:* 150
* **category** - id of the expense [category](https://github.com/AKincel18/Expensis-server/tree/development/commons#3-categories)  
  *Required:* true  
* **value** - expense value  
  *Required:* true  
  *Decimal places:* 2  
  *Max digits:* 19
  
**Example body:**
```json
{
    "date": "2021-02-10",
    "title": "title",
    "description": "description",
    "category": 1,
    "value": 1000
}
```
### Success Response

**Code:** `200 OK`

**Content example:**

```json
{
    "id": 1,
    "user": 1,
    "date": "2021-02-10",
    "title": "title",
    "description": "description",
    "category": "Food",
    "value": "1000.00"
}
```

### Error Responses

**Condition:** Negative value, empty required field, wrong date format, invalid category id

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

## 5. Remove expense

**Description:** Removes expense.

**URL:** `/expenses/{expense_id}/`

**Method:** `DELETE`

**Auth required:** Yes

### Success Response

**Code:** `204 No Content`

**Content :** `` {} ``

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

## 6. Get monthly expenses sum

**Description:** Returns expenses sum as plain text

**URL:** `/expenses-sum/`

**Method:** `GET`

**Auth required:** Yes

**Query params:**
* **year** - includes expenses from given year. Defaults by current year
* **month** - includes expenses from given month. Defaults by current month

### Success Response

**Code:** `200 OK`

**Content example:**

```
100.00
```

### Error Response

**Condition:** If access token expired.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Access token expired"
}
```
&nbsp;