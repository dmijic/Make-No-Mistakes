# Implementation review checklist

## Correctness
- Does the result satisfy the canonical specification?
- Do tests prove the requested behavior?
- Were live/external integrations validated where required?

## Architecture
- Does implementation match the current architecture?
- Were new technical facts fed back into documentation?
- Were stale assumptions accidentally reintroduced?

## Security
- Are secrets excluded?
- Are authorization boundaries enforced?
- Did any external write exceed the approved target?

## Product boundaries
- Were OPEN/TBD decisions kept open?
- Were non-goals avoided?

## Delivery
- Is startup/deployment reproducible?
- Is the repository understandable from canonical docs alone?
- Is the next pass clearly defined?
