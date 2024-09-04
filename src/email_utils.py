import imaplib
import email
from email.message import Message
from typing import Optional
from config.config import get_config

config = get_config()


def login_to_gmail() -> imaplib.IMAP4_SSL:
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(config['gmail_username'], config['gmail_password'])
    return imap


def fetch_recent_email(imap: imaplib.IMAP4_SSL) -> Optional[Message]:
    imap.select('INBOX')
    status, messages = imap.search(None, "ALL")
    email_ids = messages[0].split()
    if not email_ids:
        return None

    latest_email_id = email_ids[-1]  # Get the most recent email
    status, msg_data = imap.fetch(latest_email_id, "(RFC822)")

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            return email.message_from_bytes(response_part[1])

    return None


def is_email_from_sender(msg: email.message.EmailMessage, sender: str) -> bool:
    from_header = msg.get("From")
    return from_header and sender.lower() in from_header.lower()


def get_email_body(msg: Message) -> str:
    body = ""

    if msg.is_multipart():
        # Iterate through email parts
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            # Look for the plain text part
            if "attachment" not in content_disposition and content_type == "text/plain":
                charset = part.get_content_charset() or "utf-8"
                try:
                    body += part.get_payload(decode=True).decode(charset, errors="replace")
                except Exception as e:
                    print(f"Error decoding part: {e}")
            elif "attachment" not in content_disposition and content_type == "text/html":
                # Optionally handle HTML content
                charset = part.get_content_charset() or "utf-8"
                try:
                    html_content = part.get_payload(decode=True).decode(charset, errors="replace")
                    # Optionally, you can convert HTML to plain text using BeautifulSoup
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(html_content, "html.parser")
                    body += soup.get_text()
                except Exception as e:
                    print(f"Error decoding HTML part: {e}")
    else:
        # Not multipart - just extract the payload
        content_type = msg.get_content_type()
        if content_type == "text/plain" or content_type == "text/html":
            charset = msg.get_content_charset() or "utf-8"
            try:
                body = msg.get_payload(decode=True).decode(charset, errors="replace")
                if content_type == "text/html":
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(body, "html.parser")
                    body = soup.get_text()
            except Exception as e:
                print(f"Error decoding email body: {e}")

    return body


def get_2fa_code():
    imap_var = login_to_gmail()
    email = fetch_recent_email(imap_var)
    response = get_email_body(email).split()
    numbers = []
    for token in response:
        if not token.isdigit():
            pass
        else:
            numbers.append(token)

    return numbers[1]

