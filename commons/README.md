# **Commons**

Used to fetch static data from a database like: income ranges, age ranges and categories. 

## 1. Income ranges

**Description:** Returns the income ranges that is selected by the user during registration. Used for statistics.

**URL:** `/income-ranges`

**Method:** `GET`

**Auth required:** Yes

### Success Response

**Code:** `200 OK`

**Content example:**

```json
[
    {
        "id": 1,
        "range_from": 0,
        "range_to": 500
    },
    {
        "id": 2,
        "range_from": 500,
        "range_to": 1000
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

## 2. Age ranges

**Description:** Returns the age ranges. Used for statistics.

**URL:** `/age-ranges`

**Method:** `GET`

**Auth required:** Yes

### Success Response

**Code:** `200 OK`

**Content example:**

```json
[
    {
        "id": 1,
        "range_from": 0,
        "range_to": 18
    },
    {
        "id": 2,
        "range_from": 18,
        "range_to": 25
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

## 3. Categories

**Description:** Returns the categories that is selected by the user when adding or editing an expense. Used for statistics.

**URL:** `/categories`

**Method:** `GET`

**Auth required:** Yes

### Success Response

**Code:** `200 OK`

**Content example:**

```json
[
    {
        "id": 1,
        "value": "Food"
    },
    {
        "id": 2,
        "value": "Sport & Recreation"
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