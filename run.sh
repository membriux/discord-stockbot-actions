# DAILY_DIGEST=$(curl -s https://memo-stock-bot.herokuapp.com/daily | jq -r '.[] | "\(.name) \(.results) \n" ' | sed 's/"//g')
# curl -s -X POST "https://discord.com/api/webhooks/852683075544809512/tl6icg-eP7u-gGIRRkuZGgzp94JpxHIhiHOfI4k2UgkgeB8bGSK8gxJQjZIDjbLh3nEe" -d "content=$DAILY_DIGEST"


# curl -s localhost:5000/daily | jq -r '.[] | "\(.name) \n • \(.results) \n" ' | sed 's/"//g'
                                                                                                                
DIGEST=$(python stock_queries.py 2>&1)
echo $DIGEST
# curl -s -X POST "https://discord.com/api/webhooks/852683075544809512/tl6icg-eP7u-gGIRRkuZGgzp94JpxHIhiHOfI4k2UgkgeB8bGSK8gxJQjZIDjbLh3nEe" -d "content=$DIGEST"

# curl -s localhost:5000/daily | jq -r '.[] | "\(.name) \n - \(.results) \n" ' | sed 's/"//g'
