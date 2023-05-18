import belvo
from belvo.client import Belvo


def main() -> None:
    belvo_client = Belvo(
        secret_id="YOUR_SECRET_ID",
        secret_password="YOUR_SECRET_PASSWORD",
    )

    link = belvo_client.links.register_link(
        institution="banamex_mx_retail",
        username="username",
        password="password",
        access_mode=belvo.EnumLinkAccessModeRequest.SINGLE,
        credentials_storage="30d",
    )

    print(link)


if __name__ == "__main__":
    main()
