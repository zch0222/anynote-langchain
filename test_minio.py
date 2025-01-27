from core.oss_factory import OSSFactory
from minio import Minio
import io
from core.minio import MinIO
from core.config import MINIO_BUCKET, MINIO_ADDRESS, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BAST_PATH


if __name__ == "__main__":
    print(MINIO_ADDRESS)
    print(MINIO_ACCESS_KEY)
    oss = Minio(endpoint="192.168.100.125:9000", 
                     access_key="ESMFZJCJTZJ0UEVCKJUX",
                     secret_key="cMNNw9+Hvi32y9xoQ2bdAgoZ2E+owas9eqlpeKaO", 
                     session_token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJFU01GWkpDSlRaSjBVRVZDS0pVWCIsImV4cCI6MTczNzkyNjQ2NCwicGFyZW50IjoiYW55bm90ZSIsInNlc3Npb25Qb2xpY3kiOiJleUpXWlhKemFXOXVJam9pTWpBeE1pMHhNQzB4TnlJc0lsTjBZWFJsYldWdWRDSTZXM3NpUldabVpXTjBJam9pUVd4c2IzY2lMQ0pCWTNScGIyNGlPbHNpY3pNNlRHbHpkRUoxWTJ0bGRDSmRMQ0pTWlhOdmRYSmpaU0k2V3lKaGNtNDZZWGR6T25Nek9qbzZZMjl0Y0dGdWVXSjFZMnRsZENKZGZTeDdJbE5wWkNJNklrRnNiRzkzVlhObGNsUnZVbVZoWkZkeWFYUmxUMkpxWldOMFJHRjBZU0lzSWtWbVptVmpkQ0k2SWtGc2JHOTNJaXdpUVdOMGFXOXVJanBiSW5Nek9rZGxkRTlpYW1WamRDSXNJbk16T2xCMWRFOWlhbVZqZENKZExDSlNaWE52ZFhKalpTSTZXeUpoY200NllYZHpPbk16T2pvNlkyOXRjR0Z1ZVdKMVkydGxkQzlFWlhabGJHOXdiV1Z1ZEM4cUlsMTlMSHNpVTJsa0lqb2lSWGh3YkdsamFYUnNlVVJsYm5sQmJubFNaWEYxWlhOMGMwWnZja0ZzYkU5MGFHVnlSbTlzWkdWeWMwVjRZMlZ3ZEVSbGRtVnNiM0J0Wlc1MElpd2lSV1ptWldOMElqb2lSR1Z1ZVNJc0lrRmpkR2x2YmlJNld5SnpNenBNYVhOMFFuVmphMlYwSWwwc0lsSmxjMjkxY21ObElqcGJJbUZ5YmpwaGQzTTZjek02T2pwamIyMXdZVzU1WW5WamEyVjBJbDBzSWtOdmJtUnBkR2x2YmlJNmV5Sk9kV3hzSWpwN0luTXpPbkJ5WldacGVDSTZXMlpoYkhObFhYMHNJbE4wY21sdVowNXZkRXhwYTJVaU9uc2ljek02Y0hKbFptbDRJanBiSWtSbGRtVnNiM0J0Wlc1MEx5b2lMQ0lpWFgxOWZWMTkifQ.xYiYR1rh8yQIgAJ83BBOZr0WgnjlzEHwx5ZPl9zhYcrLrQfvGYj5dK_mMhqU50zWl8lSSwkOdC2uKt4acSPtlw",
                     cert_check=False, 
                     secure=False)
    result = oss.put_object("companybucket", "Development/2222.txt", io.BytesIO(b"TEST8"), 5)
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
                result.object_name, result.etag, result.version_id,
            ),
    )
