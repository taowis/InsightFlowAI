class ValidationAgent:
    def run(self, payload: dict) -> dict:
        # TODO: sanity checks: ranges, missing fields, anomalies
        return {"status": "ok", "validated": True}
