from fastapi import FastAPI


class APIManager:
    def __init__(self):
        self.app = FastAPI()

    def endpoint(self, route="/", method="post"):
        """
        Decorator that registers a function as a FastAPI endpoint.
        """

        def decorator(func):
            getattr(self.app, method.lower())(route)(func)
            return func

        return decorator


# Create the singleton instance
manager = APIManager()
endpoint = manager.endpoint  # Export the decorator directly
app = manager.app  # Export the app for uvicorn
