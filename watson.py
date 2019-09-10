from ibm_watson import AssistantV2
from ibm_credentials import *

assistant = AssistantV2(
    version="2019-08-20",
    url=ASSISTANT_URL,
    iam_apikey=ASSISTANT_APIKEY
)

session = assistant.create_session(ASSISTANT_ID).get_result()

# print(json.dumps(session,indent=2))
SESSION_ID = session['session_id']

def send_msg(text):
    message = assistant.message(
        ASSISTANT_ID,
        SESSION_ID,
        input = {"text": text},
        context={}
    ).get_result()

    # print(json.dumps(message,indent=2))
    responses = message['output']['generic']
    output = ""
    for r in responses:
        output += r['text']+"\n"
    return output
