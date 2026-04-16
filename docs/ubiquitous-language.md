# Ubiquitous language

Shared vocabulary for Order Manager bounded contexts. Refine as domains stabilize.

| Term | Meaning |
|------|---------|
| Order | Sale order aggregate identified by `order_id` |
| Payment | Payment attempt / capture lifecycle tied to an order |
| Shipment | Physical shipment lifecycle tied to an order |
| Saga | Orchestrated cross-service workflow (e.g. order lifecycle) |
