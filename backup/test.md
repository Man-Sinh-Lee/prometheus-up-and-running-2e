curl -u elastic:GELsUIlGH4kuRMiM7JZx --cacert /etc/elasticsearch/certs/http_ca.crt -X POST "https://4225a859241c.mylabserver.com:9200/current_fiscal_year_case/_bulk" -H 'Content-Type: application/json' --data-binary @current_fiscal_year_cases.json

curl -u elastic:GELsUIlGH4kuRMiM7JZx --cacert /etc/elasticsearch/certs/http_ca.crt https://4225a859241c.mylabserver.com:9200/_cat/nodes?v 