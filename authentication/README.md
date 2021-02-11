# **Authentication**

Used to gain or refresh access token. 

## 1. Gain token

**Description:** Returns user info with access and refresh tokens.

**URL:** `/auth`

**Method:** `POST`

**Auth required:** No

### Example request body

```json
{
    "email": "user1@u.pl",
    "password": "user1"
}
```

### Success Response

**Code:** `200 OK`

**Content example:**

```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2MTMwNjI4MDAsImlhdCI6MTYxMzA2MjUwMH0.LYtFqjcGeePxSRaurWHKvLFa9f_NsE9o9_11kZMNKSw",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2MTM2NjczMDAsImlhdCI6MTYxMzA2MjUwMH0.J6pyuuFSk271wlnp4YOTrrUeCLBsVkFhWTG26qseIGA",
    "user": {
        "id": 1,
        "email": "user1@u.pl",
        "gender": "M",
        "birth_date": "2020-12-07",
        "monthly_limit": 300.0,
        "income_range": 4,
        "date_joined": "2020-12-07T18:56:39.832949Z",
        "allow_data_collection": false
    }
}
```

### Error Response

**Condition:** If no user with given email found.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "User not found"
}
```

**Condition:** If given password is incorrect.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Wrong password"
}
```
**Condition:** If there is no email or password given.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Username and password required"
}
```
&nbsp;

## 2. Refresh token

**Description:** Returns refreshed access token.

**URL:** `/refresh`

**Method:** `POST`

**Auth required:** No

### Success Response

**Code:** `200 OK`

**Content example:**

```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2MTMwNjM4OTYsImlhdCI6MTYxMzA2MzU5Nn0.BcMUUT6yied5m6ghhzTNAoA0r9FHSAxn1URTgrTiovU"
}
```

### Error Response

**Condition:** If refresh token expired.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Expired refresh token, please login again"
}
```

**Condition:** If no refresh token given.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Authentication credentials were not provided"
}
```
**Condition:** If user coded in token is not in database.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "Authentication credentials were not provided"
}
```
**Condition:** If user coded in token is inactive.

**Code:** `403 Forbidden`

**Content:**

```json
{
    "detail": "User is inactive"
}
```
&nbsp;