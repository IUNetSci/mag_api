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
    - Result
            {
                paper_ids: [
                    xxxxxxx,
                    xxxxxxx,
                    xxxxxxx
                ]
            }
- /results/:query_id
    - GET
    - result will be null if there is an error.
    - error will be null if there is a result
    - status will be either "running" or "error" or "finished"
    - result will be a JSON object formatted depending on the original endpoint called
    - Response:
            {
                error: {...},
                result: {...},
                status: "running" or "error" or "finished"
            }
- /references/:paper_id
    - GET
    - Returns a list of paper ids for papers that the given paper references
    - Response
            {
                query_id: xxxxxx
            }
    - Result
            {
                paper_ids: [ xxxxx, xxxxx, xxxxx, xxxxx ]
            }
- /citations/:paper_id
    - GET
    - Returns a list of paper ids for papers that reference the given paper
    - Response
            {
                query_id: xxxxxx
            }
    - Result
            {
                paper_ids: [ xxxxx, xxxxx, xxxxx, xxxxx ]
            }
- /paper/:paper_id
    - GET
    - Returns details for a single paper
    - Result
            {
                paper: {
                    paper_id: xxxx,
                    doi: xxxx,
                    etc: xxxx
                }
            }
- /papers
    - POST
    - Returns details for a list of paper _ids
    - Request
            {
                paper_ids: [ xxxx, xxxx, xxxx, xxxx, xxxx, ...]
            }
    - Response
            {
                query_id: xxxxx
            }
    - Result
            {
                papers: [
                    {
                        paper_id: xxxx,
                        doi: xxxx,
                        etc: xxxx
                    },
                    ...
                ]
            }
