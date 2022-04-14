"""
 pip install google-cloud-dialogflow
"""
import os
import django
import google.protobuf.struct_pb2
from google.cloud import dialogflow_v2beta1
from google.cloud.dialogflow_v2beta1 import IntentBatch
from google.protobuf import field_mask_pb2
from chatbot.dialogflow_ID import DIALOGFLOW_PROJECT_ID, DIALOGFLOW_LANGUAGE_CODE, intent_id, training_phrase_dic

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'chatbot/private_key.json'

os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")
django.setup()

def update_entities(entity_id, entity_display_name, entity_value, entity_synonyms):
    # Create a client
    client = dialogflow_v2beta1.EntityTypesClient()

    # Initialize request argument(s)
    entity = dialogflow_v2beta1.EntityType.Entity()
    entity.value = entity_value
    entity.synonyms = entity_synonyms

    entities = dialogflow_v2beta1.EntityType(
        display_name = entity_display_name,
        name = "projects/"+DIALOGFLOW_PROJECT_ID+"/locations/global/agent/entityTypes/"+entity_id,
        kind = "KIND_MAP",
        entities = [entity]
    )

    request = dialogflow_v2beta1.UpdateEntityTypeRequest(
        language_code=DIALOGFLOW_LANGUAGE_CODE,
        entity_type=entities,
    )

    # Make the request
    response = client.update_entity_type(request=request)

    print("Waiting for operation to complete...")

    # Handle the response
    print(response,"---")


def def_intent(intent_name, response, type):
    intents_client = dialogflow_v2beta1.IntentsClient()
    parent = dialogflow_v2beta1.AgentsClient.agent_path(DIALOGFLOW_PROJECT_ID)
    training_phrases = []
    for training_phrases_part in training_phrase_dic[intent_name]:
        part = dialogflow_v2beta1.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow_v2beta1.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    if type == "text":
        message = dialogflow_v2beta1.types.Intent.Message.Text()
        message.text = [response]
        messages = dialogflow_v2beta1.types.Intent.Message(
            text = message
        )
        intent = dialogflow_v2beta1.Intent(
            display_name=intent_name,
            name="projects/" + DIALOGFLOW_PROJECT_ID + "/locations/global/agent/intents/" + intent_id[intent_name],
            training_phrases=training_phrases,
            messages=[messages],
        )
    elif type == "image":
        payload = {
            "richContent": [
                [
                    {
                        "type": "image",
                        "rawUrl": "http://matchat.shop/media/admin/eng/1.jpeg",
                        "accessibilityText": "example"
                    }
                ]
            ]
        }
        payload_struct = google.protobuf.struct_pb2.Struct()
        payload_struct.update(payload)
        message = dialogflow_v2beta1.types.Intent.Message(
            payload = payload_struct
        )
        intent = dialogflow_v2beta1.Intent(
            display_name = intent_name,
            name = "projects/"+DIALOGFLOW_PROJECT_ID+"/locations/global/agent/intents/"+intent_id[intent_name],
            training_phrases = training_phrases,
            messages = [message],
        )
    print(intent)

    return intent


def update_intent(intent_name, response):
    # Create a client
    client = dialogflow_v2beta1.IntentsClient()
    intent = def_intent(intent_name, response)

    request = dialogflow_v2beta1.UpdateIntentRequest(
        intent=intent,
    )
    # Make the request
    response = client.update_intent(request=request)
    # Handle the response
    print(response)

def update_intent2(display_name):
    client = dialogflow_v2beta1.IntentsClient()

    intent_name = client.intent_path(DIALOGFLOW_PROJECT_ID, intent_id[display_name])
    intent = client.get_intent(request={"name": intent_name})
    intent.display_name = display_name
    update_mask = field_mask_pb2.FieldMask(paths=["display_name"])
    response = client.update_intent(intent=intent, update_mask=update_mask)
    #return response



def batch_update_intents(intent_name, response):
    # Create a client
    client = dialogflow_v2beta1.IntentsClient()
    intents = list()
    for i in range(len(intent_name)):
        if i == 4:
            intents.append(def_intent(intent_name[i], response[i], "image"))
        else:
            intents.append(def_intent(intent_name[i], response[i], "text"))
    ib = IntentBatch(
        intents=intents  # intent list
    )
    request = dialogflow_v2beta1.BatchUpdateIntentsRequest(
        parent="projects/" + DIALOGFLOW_PROJECT_ID + "/locations/global/agent",
        intent_batch_uri="gs://matchat_chatbot/intents/",
        intent_batch_inline=ib,
        language_code=DIALOGFLOW_LANGUAGE_CODE,
    )
    # Make the request
    operation = client.batch_update_intents(request=request)
    print("Waiting for operation to complete...")
    # response = operation.result()
    # Handle the response
    # print(response)



