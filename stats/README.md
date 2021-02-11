# **Stats**

Used to fetch data to analyze the user's expenses presented in a graphical form (on the chart). It's three type of statistics: categories, combined and separated. All statistics have the same: url, http method and require authentication.

**URL:** `/stats`

**Method:** `POST`

**Auth required:** Yes
## 1. Categories

**Description** 
It is required that the name be equal to "Categories". Next three parameters (income range, age range and gender) filter statistics according to the values. For example: if gender set on "true", data will be filtered by the same gender as the user has. 

**Example request body:**

```json
{
    "name": "Categories",
    "filters" : {
        "income_range" : "true",
        "age_range" : "false",
        "gender" : "true"
        }
}
```

### Success Response
**Description** 
Returns as many data as there are categories. The meaning of the returned values:
- name_value: name of the category
- user_value: average cost per expense in a given category for the user
- all_value: average cost per expense in a given category for the rest of the users

**Code:** `200 OK`

**Content example:**
```json
[
    {
        "name_value": "Food",
        "user_value": 45.76,
        "all_value": 47.71
    },
    {
        "name_value": "Sport & Recreation",
        "user_value": 48.71,
        "all_value": 51.9
    },
    {
        "name_value": "Others",
        "user_value": 48.09,
        "all_value": 51.33
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

## 2. Combined

**Description** 
It is required that the name be equal to "Combined". Next three parameters (income range, age range and gender) indicate which values be returned. For example: if the gender set on "true" then a gender comparison will be returned. At least one of the parameters should be set on "true". Otherwise, an empty value will be returned. 

**Example request body:**

```json
{
    "name" : "Combined",
    "filters" : {
        "income_range" : "false",
        "age_range" : "true",
        "gender" : "true"
        }
}
```

### Success Response
**Description** 
Returns as many data as the parameters were set to true. The meaning of the returned values:
- name_value: name of statistics
- user_value: average cost per expense in a given statistics for the user
- all_value: average cost per expense in a given statistics for the rest of the users

**Code:** `200 OK`

**Content example:**

```json
[
    {
        "name_value": "Age range: 0 - 18",
        "user_value": 47.44,
        "all_value": 50.99
    },
    {
        "name_value": "Gender: Female",
        "user_value": 47.44,
        "all_value": 49.88
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

## 3. Separated

**Description** 
It is required that the name be equal to "Separated". Next three parameters (income range, age range and gender) indicate which parameter will be returned. For example: if the gender set on "true" then gender values (female and male) will be returned. Only one of the parameters should be equal to "true". If nothing set on "true", an empty value will be returned. If more than one parameter set on "true", random stats will be returned.

**Example request body:**

```json
{
    "name" : "Separated",
    "filters" : {
        "income_range" : "false",
        "age_range" : "false",
        "gender" : "true"
        }
}
```

### Success Response

**Description:** Returns data depending on the selected parameter. The meaning of the returned values:
- name_value: name of parameter value
- user_value: average cost per expense in a given parameter value for the user
- all_value: average cost per expense in a given parameter value for the rest of the users
- 
**Code:** `200 OK`

**Content example:**

```json
[
    {
        "name_value": "Female",
        "user_value": 47.44,
        "all_value": 49.88
    },
    {
        "name_value": "Male",
        "user_value": 0.0,
        "all_value": 52.63
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