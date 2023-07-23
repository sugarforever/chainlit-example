import chainlit as cl

async def start_globally():
    # Send the elements globally
    await cl.Image(path="./twitter.png", name="image1", display="inline").send()
    await cl.Text(content="Here is a side text document", name="text1", display="side").send()
    await cl.Text(content="Here is a page text document", name="text2", display="page").send()

    # Send the same message twice
    content = "Here is image1, a nice image of a cat! As well as text1 and text2!"

    await cl.Message(
        content=content,
    ).send()

    await cl.Message(
        content=content,
    ).send()

    await cl.Message(
        content="Here is image1, a nice image of a cat! As well as text1 and text3!",
    ).send()
    
async def start_scoped():
    # Send the first message without the elements
    content = "Here is image1, a nice image of a cat! As well as text1 and text2!"

    await cl.Message(
        content=content,
    ).send()

    elements = [
        cl.Image(path="./twitter.png", name="image1", display="inline"),
        cl.Text(content="Here is a side text document", name="text1", display="side"),
        cl.Text(content="Here is a page text document", name="text2", display="page"),
    ]

    # Send the second message with the elements
    await cl.Message(
        content=content,
        elements=elements,
    ).send()

    # Send the second message with the elements
    await cl.Message(
        content=content,
        elements=[
            cl.Image(path="./twitter.png", name="image1", display="inline"),
            cl.Text(content="Here is a side text document", name="text1", display="side"),
        ],
    ).send()


@cl.on_chat_start
async def start():
    await start_scoped()
