# curl -s https://memo-stock-bot.herokuapp.com/daily | jq '.[] | "\(.name) \(.results)" '
curl -s localhost:5000/daily | jq -r '.[] | "\(.name) \(.results)" ' | sed 's/"//g'