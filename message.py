
import nexmo


client = nexmo.Client(key='26e0c17f', secret='o7P1yJpNgLPziNE6')

def sms(txt):
    responseData = client.send_message(
                                    {
                                    "from": "Acme Inc",
                                    "to": '+918122382788',
                                    "text": txt,
                                    }
                                    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
