class GDriveClient:
    def __init__(self, sa_email: str, sa_key: str): ...
    def upload(self, folder_id: str, file_path: str):
        # TODO: upload to Google Drive
        return {"fileId": "..."}
