#!/usr/bin/env python3
"""list log for nginx"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    nginx_c = client.logs.nginx

    print(nginx_c.count_documents({}), "logs")
    print("Methods:")
    print("\tmethod GET:", nginx_c.count_documents({"method": "GET"}))
    print("\tmethod POST:", nginx_c.count_documents({"method": "POST"}))
    print("\tmethod PUT:", nginx_c.count_documents({"method": "PUT"}))
    print("\tmethod PATCH:", nginx_c.count_documents({"method": "PATCH"}))
    print("\tmethod DELETE:", nginx_c.count_documents({"method": "DELETE"}))

    status = nginx_c.count_documents(
                    {"method": "GET", "path": "/status"}
                        )

    print(f'{status} status check')

    for ip in nginx_c.aggregate([
        {"ip": "$ip", "count": {"$count": "$ip"}}
        ]):
        print(ip)
