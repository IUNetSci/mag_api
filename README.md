# M.A.G. REST API

## Endpoints

All endpoints return either a query ID or an error message

- /search
    - POST
    - Request
            {
                return_type: "json" or "csv",
                years: [1901, 1902, etc],
                title: "xxxxx",
                author: "xxxxxx",
                doi: "xxxxx"
            }
    - Response
            {
                query_id: xxxxxx
            }
- /results/:query_id
    - GET
    - result will be null if there is an error.
    - error will be null if there is a result
    - Response:
            {
                error: {...},
                result: {...},
                status: "running" or "error" or "finished"
            }
