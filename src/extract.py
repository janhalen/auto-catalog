import json
import airbyte as ab

def main() -> None:
    read_result = ab.get_source(
        "source-github",
        config={
            "start_date": "2020-01-01T00:00:00Z",
            "access_token": ab.get_secret("GITHUB_PERSONAL_ACCESS_TOKEN"),
        },
        streams=["organizations"],
    ).read()

    data = [message.record.data for message in read_result if message.type == Type.RECORD]

    with open('_data/organizations.json', 'w') as f:
        json.dump(data, f)