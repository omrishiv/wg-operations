import uvicorn
# Import routes to register them
import agent_entry
from api_manager import manager

# Export the app
app = manager.app

uvicorn.run(app, host="0.0.0.0", port=8000)
