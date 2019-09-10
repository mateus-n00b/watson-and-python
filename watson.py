from ibm_watson import AssistantV2
from ibm_credentials import *

def login():
    try:
        assistant = AssistantV2(
            version="2019-08-20",
            url=ASSISTANT_URL,
            iam_apikey=ASSISTANT_APIKEY
        )

        session = assistant.create_session(ASSISTANT_ID).get_result()
        return session
    except Exception as e:
        print(e)
        exit(-1)

# print(json.dumps(session,indent=2))

def send_msg(text):
    session = login()
    SESSION_ID = session['session_id']
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
