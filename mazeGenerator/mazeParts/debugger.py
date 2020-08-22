import logging


class Debugger(object):
    logFile = f"./mazeGenerator/logs/{__name__}.log"

    formatter = logging.Formatter("%(message)s")

    # LOGGER = logging.getLogger(logFile)
    # LOGGER.setLevel(logging.DEBUG)
    # file_handler = logging.FileHandler(logFile)
    # file_handler.setFormatter(formatter)
    # file_handler.setLevel(logging.DEBUG)

    STREAMER = logging.getLogger(__name__)
    STREAMER.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)

    # LOGGER.addHandler(file_handler)
    STREAMER.addHandler(stream_handler)
