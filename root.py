# faust -A root worker --web-port 30001

import faust
from topics import root as topic_root


app = faust.App(
    id='test-root',
    broker='localhost:9092',
    topic_partitions=1
)

root_topic = topic_root.init(app)


@app.agent(root_topic)
async def hello(greetings):
    async for greeting in greetings:
        print(greeting)


@app.timer(interval=10.0)
async def example_sender():
    await hello.send(
        key='III',
        value='Hello Root War III',
    )

if __name__ == '__main__':
    app.main()
