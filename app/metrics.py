from prometheus_client import Counter, Histogram, Gauge, Info

# Service info
APP_INFO = Info('inventory_service', 'Inventory Service Information')

# Request metrics (Golden Signals)
REQUEST_COUNT = Counter(
    'inventory_requests_total',
    'Total number of requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'inventory_request_duration_seconds',
    'Request latency in seconds',
    ['method', 'endpoint']
)

# Business metrics (this makes it stand out)
STOCK_UPDATES = Counter(
    'inventory_stock_updates_total',
    'Total stock updates performed',
    ['product_id', 'action']
)

CURRENT_STOCK = Gauge(
    'inventory_current_stock',
    'Current stock level for product',
    ['product_id']
)

ERROR_COUNT = Counter(
    'inventory_errors_total',
    'Total errors encountered',
    ['type']
)
