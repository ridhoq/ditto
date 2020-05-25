import markovify

from .cache import CacheRepository
from .cosmos import cosmos


def get_model(user, cache_repo: CacheRepository):
    if user in cache_repo:
        model_json = cache_repo[user]
        return markovify.NewlineText.from_json(model_json)

    messages = [item["text"] for item in cosmos.get_message_events_for_user(user)]
    newline_delimited_messages = "\n".join(messages)
    model = markovify.NewlineText(newline_delimited_messages)
    model.compile(inplace=True)
    cache_repo[user] = model.to_json()

    return model
