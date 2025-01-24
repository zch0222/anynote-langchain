from core.oss_factory import OSSFactory
from minio import Minio
import io
from core.minio import MinIO
from core.config import MINIO_BUCKET, MINIO_ADDRESS, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BAST_PATH


if __name__ == "__main__":
    print(MINIO_ADDRESS)
    print(MINIO_ACCESS_KEY)
    oss = Minio(endpoint=MINIO_ADDRESS, 
                     access_key=MINIO_ACCESS_KEY,
                     secret_key=MINIO_SECRET_KEY, cert_check=False, secure=False)
    result = oss.put_object(MINIO_BUCKET, "test.txt", io.BytesIO(b"TEST"), 4)
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
                result.object_name, result.etag, result.version_id,
            ),
    )
