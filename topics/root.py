from faust import App, TopicT


def init(app: App) -> TopicT:
    return app.topic('test-root', key_type=str,
                     value_type=str, value_serializer='json', partitions=1)
