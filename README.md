# JSONexusSync Python Client Documentation

## Introduction

The JSONexusSync Python client library provides an easy-to-use interface for interacting with JSONexusSync remote database system using WebSockets.

## Installation

You can install the JSONexusSync Python client library using pip:

    pip install jsonexussync-client

## Usage

Here's an example of how to use the JSONexusSync Python client library:

```python
    import asyncio
    import json
    from jsonexussync_client import JSONexusSyncClient

    async def main():
        config = config = {
            "api_key":"YourApiKey",
            "server_uri": "ws://localhost:8765"
            }
        client = JSONexusSyncClient(config)

        # Insert a new item into the 'users' collection
        await client.insert_data('users', {'name': 'Charlie', 'age': 35, 'email': 'charlie@example.com'})

        # Find users with a specific query
        result = await client.find_data('users', {'age': {'_op': '$eq', '_value': 35}})
        print(result)

        # Delete users with a specific query
        await client.delete_data('users', {'name': {'_op': '$eq', '_value': "Melissa Villarreal"}})

        # Update users with a specific query
        result = await client.update_data('users', {"age": {'_op': '$eq', '_value': 23}}, {"job": "Ethical Hacker"})

        # Creating a new database
        result = await client.create_db('txns')

        # Generate an API key
        result = await client.generate_api_key('adminr', 'db')

        # Creating a new database
        result = await client.create_db('companys')

        #result = await client.get_dbs()

        #result = await client.create_collection("students")
        print(result)

    if __name__ == "__main__":
        asyncio.run(main())
```
## Conclusion

The JSONexusSync Python client library simplifies interaction with JSONexusSync remote database system, allowing developers to easily integrate real-time data synchronization into their Python applications.

For more information and detailed documentation, please visit the [JSONexusSync Documentation](https://jsonexus.gitbook.io/jsonexussync/).
