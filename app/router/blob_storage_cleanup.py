from fastapi import APIRouter
from datetime import datetime, timedelta, timezone
from vercel_storage.blob import list, delete
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

@router.get("/blob-storage-cleanup", tags=["Blob Storage Cleanup"])
async def blob_storage_cleanup():
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=1)

    print(f"Running cleanup... | Current time: {now.isoformat()} | Cutoff time (1 day ago): {cutoff.isoformat()}")

    blobs = list({"prefix": "temp"}).get("blobs", [])
    deleted = 0

    for blob in blobs:
        uploaded_at = datetime.fromisoformat(blob["uploadedAt"].replace("Z", "+00:00"))
        if uploaded_at < cutoff:
            print(f"Deleting blob: {blob['pathname']} (Uploaded at: {uploaded_at})")
            delete(blob["pathname"], options={})
            deleted += 1

    return {
        "statusCode": 200,
        "body": f"Cleanup complete. Deleted {deleted} blobs older than a day."
    }
