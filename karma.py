import description_parser


class Karma:
    def __init__(self, app):
        self.app = app

    def __get_user_email(self, user_id):
        try:
            user_info = self.app.client.users_info(user=user_id)
            profile = user_info['user']['profile']
            email = profile.get("email")
            return email
        except Exception as e:
            print(f"Failed to fetch user info for {user_id}: {e}")
            return None

    def parse_karma_event(self, event):
        karma_text = event.get("attachments", [])[0].get("title", "")
        number_of_karmas = (
            int(karma_text.split("+")[-1].strip()) if "+" in karma_text else 0
        )

        user_ids = []
        for block in event.get("blocks", []):
            for element in block.get("elements", []):
                if element.get("type") == "rich_text_section":
                    for item in element.get("elements", []):
                        if item.get("type") == "user":
                            user_ids.append(item.get("user_id"))

        image_url = event['attachments'][0]['image_url']
        description = description_parser.parse(image_url)

        return {
            "karmas": number_of_karmas,
            "users": [self.__get_user_email(user) for user in user_ids],
            "reason": (
                description
                .replace("\n", "")
                .replace("\\n", "")
                .replace(">*", "")
                .replace(">/", "")
            )
        }


def test(app, event):
    def _get_user_full_name(user_id):
        try:
            user_info = app.client.users_info(user=user_id)
            profile = user_info['user']['profile']
            full_name = profile.get("real_name") or profile.get("display_name")
            print(f"====> user id {user_id}, name: {full_name}")
            return full_name
        except Exception as e:
            print(f"Failed to fetch user info for {user_id}: {e}")
            return None

    def _parse_karma_message(event):
        karma_text = event.get("attachments", [])[0].get("title", "")
        number_of_karmas = int(karma_text.split("+")[-1].strip()) if "+" in karma_text else 0

        user_ids = []
        for block in event.get("blocks", []):
            for element in block.get("elements", []):
                if element.get("type") == "rich_text_section":
                    for item in element.get("elements", []):
                        if item.get("type") == "user":
                            user_ids.append(item.get("user_id"))

        image_url = event['attachments'][0]['image_url']
        description = description_parser.parse(image_url)

        return {
            "karmas": number_of_karmas,
            "users": [_get_user_full_name(user) for user in user_ids],
            "reason": (
                description
                .replace("\n", "")
                .replace("\\n", "")
                .replace(">*", "")
                .replace(">/", "")
            )
        }

    print("========== event", event)
    karma_detail = _parse_karma_message(event)
    print(karma_detail)
