import os

from prefect import flow
from prefect.runner.storage import GitRepository

@flow(log_prints=True)
def my_flow():
    print("Hello again and again and again, world!")

if __name__ == "__main__":
    my_flow()
