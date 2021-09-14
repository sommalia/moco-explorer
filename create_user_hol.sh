curl -X POST \
  'https://testabcd.mocoapp.com/api/v1/users/holidays' \
  -H 'Authorization: Token token=1dbfb5d766343983ab5642c2b939a8c9' \
  -H 'Content-Type: application/json' \
  -d '{
        "user_id": 933640035,
        "year": 2020,
        "title": "uha",
        "hours": 20,
      }'