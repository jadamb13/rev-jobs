import imaplib
import email
from email.header import decode_header
from typing import Optional


def login_to_gmail(username: str, password: str) -> imaplib.IMAP4_SSL:
    """Logs in to Gmail using IMAP and returns the IMAP client."""
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    return imap


def fetch_recent_email(imap: imaplib.IMAP4_SSL) -> Optional[email.message.EmailMessage]:
    """Fetches the most recent email from the inbox."""
    imap.select("inbox")
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
    """Checks if the email is from the specified sender."""
    from_header = msg.get("From")
    return from_header and sender.lower() in from_header.lower()


def get_email_body(msg: email.message.EmailMessage) -> str:
    """Extracts and returns the body of the email."""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if "attachment" not in content_disposition and content_type == "text/plain":
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()

    return ""