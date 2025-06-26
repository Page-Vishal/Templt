
def load_content() -> str:
    """
    Args:
        None
    Return:
        The HTML body as str to be loaded
    """
    content = """
    <body>
    <form action= "/pdf" method="post" enctype="multipart/form-data">
        <input name ="file" type= "file">
        <input type= "submit">
    </form>
    </body>

    """

    return content